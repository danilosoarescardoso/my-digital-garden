---
title: Resumão para Certificação AZ-900
date: 2020-09-12 20:18:55
---

Durante a pandemia, a Microsoft disponibilizou inúmeros vouchers para a certificação AZ-900. Segundo a própria Microsoft,

> Este exame é projetado para candidatos que procuram demonstrar conhecimento de nível fundamental de serviços de nuvem e como esses serviços são fornecidos com Microsoft Azure.

Sendo assim, se você precisa lidar - ou planeja trabalhar futuramente - com qualquer ambiente de nuvem, esteja ele na Azure ou não, vale a pena tirar essa certificação. A certificação AZ-900 aborda não apenas os aspectos que a Microsoft atende com o Azure, como também envolve assuntos relacionados à *cloud computing* em geral, como escalabilidade, elasticidade, virtualização e segurança. Vale ressaltar que ela é indicada não apenas para desenvolvedores e profissionais técnicos, mas também para gestores em geral que precisem tomar decisões em projetos na nuvem. a Microsoft diz que:

> O exame destina-se a candidatos sem formação técnica, como os envolvidos na venda ou compra de soluções e serviços com base em nuvem ou que tenham algum conhecimento em soluções e serviços baseados em nuvem, bem como aqueles com formação técnica e que precisam validar seu nível de conhecimento fundamental em serviços em nuvem. A experiência técnica de TI não é exigida, mas requer algum conhecimento ou experiência geral de TI.


Abaixo fiz uma lista dos assuntos que estão no [documento de Skills Avaliadas](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE3VwUY) válido até 15 de Setembro de 2020. Após essa data os conteúdos poderão mudar.

## Tópicos importantes

### 1. [Entendendo conceitos de cloud](https://docs.microsoft.com/pt-br/learn/modules/principles-cloud-computing/3-benefits-of-cloud-computing) (15-20%)

#### Benefícios e considerações ao usar cloud

* Termos importantes
  * **high availabilty**: é o conceito que mensura o tanto de tempo que um site ou sistema fica de pé durante um determinado período
  * **scability**: habilidade que um sistema tem de se manter online de acordo com o uso dos usuários (quanto mais usuários, mais escalabilidade)
  * **elasticity**: habilidade do sistema de automaticamente diminuir ou aumentar baseado na demanda
  * **agilidade**: habilidade de mudar rapidamente baseado no mercado ou ambiente
  * **tolerança a falhas**: habilidade de lidar com falhas, como falta de energia, rede, ou falhas de hardware
  * **disaster recovery**: capacidade de se recuperar de falhas e o tanto de informações que pode ser perdidade e em quanto tempo irá retornar
  * **[economia de escala](https://docs.microsoft.com/en-us/learn/modules/principles-cloud-computing/3b-economies-of-scale)**: é muito barato para a Microsoft criar um novo servidor, mais do que conseguiríamos criar um dia. Quanto mais você cria, mais barato é para usar.
  * **Capex**: Dinheiro gasto em assets (como computadores) que vão retornar um valor de investimento
  * **Opex**: é o valor gasto todos os dias em operações diárias. Na relação Capex Opex, **Azure permite que você use Opex ao invés de Capex como investimento.**
  * **[Diferenças entre CapEx e OpEx](https://docs.microsoft.com/en-us/learn/modules/principles-cloud-computing/3c-capex-vs-opex)**
  * **[modelo baseado em consumo](https://www.serverless360.com/blog/consumption-vs-dedicated-billing-models)**: serviços de cloud são cobrados de acordo com o uso
   

#### Paradigmas de Hospedagem
*  [Infrastructure-as-a-Service (IaaS)](https://azure.microsoft.com/pt-br/overview/what-is-iaas/)
*  [Platform-as-a-Service (PaaS)](https://azure.microsoft.com/pt-br/overview/what-is-paas/)
*  [Software-as-a-Service (SaaS)](https://azure.microsoft.com/pt-br/overview/what-is-saas/)

#### Tipos de Nuvem

* [Cloud Privada](https://www.totvs.com/blog/inovacoes/tipos-de-cloud-computing)
* Cloud Pública
* Cloud Híbrida
   
### 2. Core Azure Services (30-35%) 
* Componentes de Arquitetura
  * **[Regiões](https://docs.microsoft.com/pt-br/azure/availability-zones/az-overview)**: até maio de 2020 existiam mais de 60 regiões diferentes
  * **Zonas de Disponibilidade**: se você precisa que suas aplicações estejam disponíveis em diferentes servidores, devido a riscos de desastres naturais, por exemplo, é possível fazer isso, mas apenas em algumas regiões.
  * **[Grupos de Recurso](https://docs.microsoft.com/pt-br/azure/azure-resource-manager/management/manage-resource-groups-portal):** são uma espécie de pasta com todos os recursos para determinado projeto. No caso do GEOTEC, por exemplo, estão todas as instâncias de banco, aplicação e logs.
  * **[Azure Resource Manager](https://docs.microsoft.com/pt-br/azure/azure-resource-manager/management/overview)**: é algo relativamente novo. É uma API para você ter funcionalidades em comum para gerenciar seus resource. 
  * Benefícios na utilização de componentes arquiteturais do core do Azure

* Azure Core Products
  * Compute
    * Em resumo, é quando você executa código na cloud
    * Pode ser um site, batch process, etc
    * Tipos de Recurso
        + Virtual Machines
            * IAAS
            * É quando você tem uma máquina na cloud, windows ou linux
            * existem diferentes versões de windows e linux disponíveis
            * você tem controle total, como se fosse sua máquina
            * sendo uma máquina virtual, é uma espécie de pedaço de uma máquina física dividida com outros consumidores
            * hoje existem +200 diferentes opções de VM para escolher
        + Virtual Machines Scale Sets
            * múltiplas VMs rodando atrás de um load balancer
            * alta disponibilidade para que sua aplicação não pare caso seja feito um deploy ou reboot qualquer
            * escala horizontal 'infinita', adicionando mais máquinas
            * escala vertical limitada tendo em vista que existe um tipo específico de máquina rodando
        + App Services
            * um novo paradigma para rodar código na cloud
            * você concede o código e a configuração e a Azure roda
            * promessa de performance mas sem acesso ao hardware
            * PAAS
        + Containers
            * Outro paradigma para rodar código na cloud
            * uma imagem contém tudo o que a aplicação precisa para rodar
            * rápido e fácil para fazer deploy
            * [Azure Container Instances - ACI](https://azure.microsoft.com/pt-br/services/container-instances/)
                - single instance, quickest way to deploy a container
            * [Azure Kurbenetes Services - AKS](https://azure.microsoft.com/pt-br/services/kubernetes-service/)
                - run on a cluster of servers, enterprise grade
---
  * Networking
    * Connectivity services
      - Virtual Network
        + emula uma rede física, é sempre necessário para criar uma máquina virtual
        + toda rede pode ser dividida em uma ou mais subnets
        + network security groups protegem as virtual networks 
      - VPN
        + mesmo conceito clássico de VPN, mas no Azure
        + é possível conectar em uma rede da Azure a partir de uma rede física, como a da sua empresa
      - ExpressRoute
        + é uma fibra ótica física conectada entre um datacenter Azure e sua rede. Não passa pela rede pública
        + é ultraveloz mas é caro      
    * Protection Services
      -  DDos Protection
        + Azure possui uma camada básica de proteção contra ataques DDoS
        + Não inclui proteção para as aplicação especificamente  
      -  Azure Firewall
        + Para proteção dos aplicativos é necessário usar o Azure Firewall
      -  Network Security Groups
        + Grupos gratuitos com regras para controle de acesso
        + se o tráfego não respeitar as regras, ele é interrompido  
      -  Private Link  
    * Delivery Services
      - Load Balancer
        + distribuição de tráfego entre servidores
      - Application Gateway
        + load balancer mais elevado, com firewall opcional
      - CDN
      - Azure Front Door Service
        + load balancer + CDN + firewall 
    * Monitoring Services
      - Network Watcher: verificar trafégo para debug
      - ExpressRoute Monitor: monitor para o ExpressRoute
      - Azure Monitor: same thing 
  
___

  * Storage
    * Unmanaged Storage
      - general purpose v2: indicado para 99,9% dos usuários
        + quatro tipos de arquivos: blobs, tables, queues, files
      - azure data lake storage
        + é desenhado para big data
        + feito para armazenar vários petabytes de dados
        + tipo mais barato de armazenamento
        + 1.8 cents per GB

    * Options de unmanaged storage
      - Access tiers
        + hot, cool e archive
        + é uma forma de precificar o armazenamento dos dados dependendo de como o acesso a eles será necessário
        + hot: acesso frequente
        + cool: acesso moderado
        + archive: usar o armazenamento como um backup, por exemplo
      - Performance Tiers:
        + standard ou premium
        + está relacionado com a velocidade em que você terá acesso a estes dados
      - Location
        + é indicado escolher o lugar mais próximo dos usuários para evitar problemas com rede, como demora ou alta latência
      - Redundancy / replication
        + formas de replicar e redundar os dados de forma a manter cópias de segurança em caso de falhas 
      - Failover options
        + duas storage accounts, se você perder a primeira, a segunda terá acesso para que você recupere o que perdeu

    * Managed Disks
      - quase que exclusivamente reservado para VM disks
      - a recomendação da microsoft é usar esse tipo de disco para usar em VMs
      - é um pouco mais caro que os unmanaged storages
      - a precificação muda, você pagará pelos GBs que reservar, mesmo que não use tudo 

* Backup, Replication and Recovery Storage
    - serviço do Recovery Services Vault
        + backup storage
        + é possível salvar neles backups de servidores locais com Azure Job
    - Possui back policies
    - Para usar replicação, existe o serviço Azure Site Recovery
        + Permite, por exemplo, duplicar uma região em outra
        + os arquivos dessa replicação serão armazenados em um Recovery Services Vault 

---
  * Databases
    * Cosmos DB
      - storage extremamente rápido
      - desenhado para aplicações modernas como jogos, redes sociais e aplicações que recebem milhares de requisições diariamente
      - base NoSQL 
      - multi modal e suporta inúmeros tipos de extensões de dados a serem salvos
      - suporta uma grande variedade de APIs e protocolos open source
    * Azure SQL Database
      - usa o SQL Server por baixo dos panos
      - banco de dados relacional
      - Database As A Service
      - Fácil de replicar
      - Fácil de escalar
      - Fácil de migrar de uma instalação on premise
    * Azure Database for MySQL
      - Banco de dados MySQL gerenciado
      - banco de dados open source bastante comum no mercado
      - Fácil migração para a cloud
    * Azure Database for PostgreeSQL
      - Banco de dados MySQL gerenciado
      - banco de dados open source
      - tem suporte otimizado para clusters e servidores com configuração complexa
    * Azure Database Migration Service
      - Serviços e ferramentas para a sua jornada de migração
    * Azure Synapse Analytics (SQL DW)
      - Não faz parte do exame
      - criado para big data
      - antigamente se chamava SQL Data Warehouse
      - faz pré-processamento dos dados para que as consultas sejam mais rápidas
      - Base de dados analítica, não transacional
    * [Serviços de migração](https://azure.microsoft.com/pt-br/services/database-migration/)
    * [Azure Marketplace](https://azure.microsoft.com/pt-br/marketplace/) e cenários de uso

---

* Soluções
  * Internet of Things (IoT)
    - IoT Hub
        + serviço para gerenciar a comunicação entre seu aplicativo IoT e os dispositivos gerenciados por ele.
    - IoT Central
        + solução de SaaS (software como serviço) de IoT global e totalmente gerenciada que facilita a conexão, o monitoramento e o gerenciamento dos seus ativos de IoT em escala.
  * Big Data e Analytics
    - [Azure Synapse Analytics](https://azure.microsoft.com/pt-br/services/synapse-analytics/)
    - HDInsight
        + Serviço para análise de software livre (Hadoop, Kafka, Spark)
        + Seve para processamento sem esforço de grandes quantidades de dados
    - Azure Databricks
        + ajuda na manipulação de big data
        + serviço centralizado para recebimento e manipulação de dados
        + permite análise e criação de relatórios para fins de inteligência de negócios
  * Inteligência Artificial (IA)
    - Azure Machine Learning Service 
        + Faz parte da família de [Serviços cognitivos](https://azure.microsoft.com/pt-br/services/cognitive-services/)
        + Exemplo de serviços
            * Vision API: descoberta de conteúdo como texto a partir de imagens 
            * Language Service : recebe o que é falado por microfone e retorna texto
  * **Serverless**: Serviço para subir código ao Azure sem se preocupar com infraestrutura
    - [Azure Functions](https://docs.microsoft.com/pt-br/azure/azure-functions/functions-overview)
    - [Logic Apps](https://docs.microsoft.com/pt-br/azure/logic-apps/logic-apps-overview)
    - [Event grid](https://azure.microsoft.com/pt-br/services/event-grid/#overview)
  * [Azure DevOps](https://azure.microsoft.com/pt-br/overview/what-is-devops/)
  * [Azure DevTest Labs](https://azure.microsoft.com/pt-br/services/devtest-lab/#overview)

---

* Azure Management Tools
  * Azure CLI
    *  CLI é um acrônimo para command line interface, ou seja, comandos que podem ser executados pelo usuário a partir de um console
    *  O CLI do Azure permite criar, editar excluir recursos como discos e VMs
    *  Baseado em bash scripting, comum no Linux 
  * PowerShell
    * é uma plataforma da Microsoft que permiet a automatação de tarefas através de scripts.
    * No Azure é possível criar, gerenciar e exluir Azure Resources a partir de scripts
  * Azure Portal
    * Site da azure onde você pode gerenciar todo os recursos disponíveis e adquiridos na Azure
  * Azure Cloud Shell
    * shell interativo, autenticado e acessível pelo navegador para o gerenciamento de recursos do Azure. Ele dá a você a flexibilidade de escolher a experiência de shell que melhor se adequa ao modo como você trabalha, seja com o Bash ou o PowerShell.
  * Azure Advisor
    * Serviço que permite monitorar todos os seus recursos de uma vez, recomendnado o que pode ser melhorado em termos de configuração e custos
    * Monitora disponibilidade, segurança, performance e custo

---

###  3. Security, Privacy, Compliance, and Trust (25-30%)

* atualizando...

---

### 4. Azure Pricing, Service Level Agreements, and Lifecycles (20-25%)

* atualizando...

tags: [[tecnologia]], [[arquitetura]]