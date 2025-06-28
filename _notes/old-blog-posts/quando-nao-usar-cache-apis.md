---
title: Quando não usar cache em suas APIs
date: 2023-04-15 12:27:00

---

Dias atrás fiz um [post falando sobre quando devemos utilizar cache em APIs](https://danilocardoso.dev/blog/quando-usar-cache-apis/). No texto de hoje apresento alguns casos onde cache não deve ser utilizado:

⏩ 𝐃𝐚𝐝𝐨𝐬 𝐚𝐥𝐭𝐚𝐦𝐞𝐧𝐭𝐞 𝐝𝐢𝐧â𝐦𝐢𝐜𝐨𝐬: Se os dados retornados pela API mudam constantemente ou são únicos a cada requisição, o uso de cache não será eficiente e pode até mesmo retornar informações desatualizadas ou incorretas.

🔒 𝐃𝐚𝐝𝐨𝐬 𝐬𝐞𝐧𝐬í𝐯𝐞𝐢𝐬 𝐨𝐮 𝐜𝐨𝐧𝐟𝐢𝐝𝐞𝐧𝐜𝐢𝐚𝐢𝐬: Se a API lida com informações sensíveis, como dados pessoais ou informações financeiras, o cache pode representar um risco à segurança, uma vez que esses dados podem ser acessados indevidamente se os acessos não forem gerenciados corretamente.

📉 𝐁𝐚𝐢𝐱𝐨 𝐯𝐨𝐥𝐮𝐦𝐞 𝐝𝐞 𝐫𝐞𝐪𝐮𝐢𝐬𝐢çõ𝐞𝐬: Se a API não recebe um volume alto de requisições, o uso de cache pode não ser necessário e pode até mesmo aumentar a complexidade e os recursos necessários para manter o sistema.

📝 𝐀𝐏𝐈𝐬 𝐝𝐞 𝐞𝐬𝐜𝐫𝐢𝐭𝐚: APIs que realizam ações, como criar, atualizar ou excluir recursos geralmente não se beneficiam do cache. O cache é mais eficaz para operações de leitura, onde os dados são consultados, mas não modificados. Entretanto, há exceções, como no caso de APIs que precisem de idempotência para impedir ações duplicadas. 

🕟 𝐓𝐞𝐦𝐩𝐨 𝐫𝐞𝐚𝐥 𝐨𝐮 𝐥𝐚𝐭ê𝐧𝐜𝐢𝐚 𝐜𝐫í𝐭𝐢𝐜𝐚: Se a aplicação requer acesso a dados em tempo real ou tem requisitos de latência muito baixos, o uso de cache pode não ser adequado. Nestes casos, pode ser necessário otimizar a API e a infraestrutura para atender a essas demandas específicas.

Ao projetar e implementar APIs, é importante avaliar cuidadosamente as necessidades de desempenho e escalabilidade e, em seguida, decidir se o uso de cache é apropriado. Em alguns casos, pode ser mais benéfico otimizar a própria API ou a infraestrutura relacionada para melhorar o desempenho sem recorrer ao cache.

Como é comum dizer em arquitetura, tudo vai depender dos trade-offs escolhidos.

tags: [[APIs]], [[arquitetura]]