---
title: "Gerenciando sessões autenticadas em Java com Redis"
date: 2025-11-02 18:01:00
---

Estava com saudades de programar e escrever sobre. Essa semana surgiu um desafio bacana: impedir múltiplas sessões autenticadas em um *backend for frontend* feito em Java. Como Arquiteto de Software, a minha indicação inicial foi utilizar os mecanismos do próprio Spring Security, que permitem definir quantas sessões múltiplas são possíveis. O problema foi: como fazer isso em ambientes distribuídos?

Nesse cenário é impossível garantir, apenas usando bibliotecas, que não existem duas sessões simultâneas para um mesmo usuário, já que a gestão de identidade das diferentes sessões é feita de forma individual, por cada instância. Quando isso ocorre, uma das soluções possíveis é gerenciar as sessões de forma centralizada, ou seja, armazenar dados referentes ao login e sessão ativa, para garantir que a pessoa tenha apenas uma sessão.

Após algumas pesquisas e conversas com colegas, cheguei nessa implementação final.

## Implementação técnica

Sendo um projeto Java com Maven, é necessário usar as seguintes bibliotecas:

```xml
<dependencies>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-data-redis</artifactId>
	</dependency>
	<dependency>
		<groupId>org.springframework.session</groupId>
		<artifactId>spring-session-data-redis</artifactId>
	</dependency>
 </dependencies>
```

A biblioteca **spring-boot-starter-data-redis** é responsável por criar as interfaces entre uma instância Redis e sua aplicação, enquanto a **spring-session-data-redis** permite que haja a persistência de objetos de sessão no Redis.

O próximo passo é criar um bean de configuração de segurança, seguindo esses passos:

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http, SessionRegistry sessionRegistry, LogoutHandler logoutHandler) throws Exception {
    AuthLoggingSuccessHandler successHandler = new AuthLoggingSuccessHandler("/");
    AuthLoggingFailureHandler failureHandler = new AuthLoggingFailureHandler("/login?error=true");
    
    http
        .authorizeHttpRequests(auth -> auth
            .requestMatchers(
                "/h2-console/**",
                "/login",
                "/j_security_check",
                "/css/**",
                "/js/**",
                "/.well-known/**",
                "/error"
            ).permitAll()
            .anyRequest().authenticated()
        )
        .formLogin(form -> form
            .loginPage("/login")
            .loginProcessingUrl("/j_security_check")
            .successHandler(successHandler)
            .failureHandler(failureHandler)
            .usernameParameter("j_username")
            .passwordParameter("j_password")
            .permitAll()
        )
        .logout(logout -> logout
            .logoutUrl("/perform_logout")
            .addLogoutHandler(logoutHandler)
            .logoutSuccessUrl("/login?logout=true")
            .permitAll()
        )
        // liberar frames e CSRF para o console H2
        .headers(headers -> headers.frameOptions(frame -> frame.disable()))
        .csrf(csrf -> csrf.ignoringRequestMatchers(
            request -> request.getServletPath().startsWith("/h2-console"),
            request -> request.getServletPath().equals("/j_security_check")
        ))
        .sessionManagement(session -> session
            .maximumSessions(1)
            .maxSessionsPreventsLogin(true)
            .expiredUrl("/login?expired=true")
            .sessionRegistry(sessionRegistry))
        .sessionManagement(session -> session
            .sessionFixation().migrateSession());

    logger.info("Configuração de segurança inicializada com limite de 2 sessões por usuário");

    return http.build();
}
```


No código acima, defini um filtro em que toda requisição HTTP passe por ele. Foram criados também dois *handlers*, um pra quando há sessão autenticada e outro para o inverso, que trazem logs do processo. No restante do código são definidas quais URLs podem ser acessadas sem autenticação, e para a autenticação, quais os parâmetros necessários. Na parte de SessionManagement, definimos uma sessão como o máximo possível simultaneamente.

Por fim, incluí a linha *.sessionManagement(session -> session.sessionFixation().migrateSession())* para, no momento em que uma nova autenticação ocorrer, levar em consideração a sessão atual e invalidar qualquer outra. Foi criada a classe SessionCleanupLogoutHandler para invalidar o cache quando um logout for feito. 


Para que as sessões sejam salvas, basta criar essa classe, pois ela ficará responsável por lidar com o registro das sessões ativas no Redis.

```java
package com.froiscardoso.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.core.session.SessionRegistry;
import org.springframework.security.core.session.SessionRegistryImpl;
import org.springframework.session.data.redis.config.annotation.web.http.EnableRedisHttpSession;

@Configuration
@EnableRedisHttpSession(maxInactiveIntervalInSeconds = 1800)
public class SessionConfig {

    @Bean
    public SessionRegistry sessionRegistry() {
        return new SessionRegistryImpl();
    }
}

```



<b>tags:</b> [[desenvolvimento]], [[tecnologia]], [[arquitetura]]