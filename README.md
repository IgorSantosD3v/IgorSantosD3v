Header Typing SVG [![LinkedIn](https://img.shields.io/badge/LinkedIn-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/igor-santos-devzao) [![Email](https://img.shields.io/badge/Email-ea4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Igorsantosdevp@gmail.com) [![Instagram](https://img.shields.io/badge/Instagram-e1306c?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/igorp.y/?hl=en) [![GitHub](https://img.shields.io/badge/IgorSantosD3v-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/IgorSantosD3v) ![Views](https://komarev.com/ghpvc/?username=IgorSantosD3v&style=for-the-badge&color=0a66c2&label=VIEWS)
Índice
Sobre mim
O que estou construindo agora
Experiência
Projetos em destaque
Tecnologias
Formação
Trajetória
GitHub
Contato
Sobre mim
Sou desenvolvedor back-end e fundador de produto. Trabalho principalmente com Python (FastAPI) e C# (ASP.NET, ASP.NET MVC), construindo APIs REST, integrações com IA generativa e sistemas que lidam com dinheiro de verdade, mensagens de verdade e clientes de verdade. Passei pelo desenvolvimento corporativo na Wooba, mantendo fluxos de busca de voos e hotéis de uma plataforma de viagens em produção, e hoje toco a **Flow**, minha marca de produtos SaaS. O principal deles é o **AgendaFlow**, um sistema de agendamento via WhatsApp com atendimento por IA, pagamentos PIX e painel administrativo, rodando em produção. Antes da tecnologia, trabalhei na operação de indústrias farmacêuticas, e isso ficou: gosto de processo, de rastreabilidade e de sistema que não quebra quando o volume aumenta. Curso Engenharia de Software na FIAP e Desenvolvimento Back-end Python na EBAC, e sigo estudando System Design, Clean Architecture, cloud e inglês para atuar em times internacionais. **Buscando:** vaga de Desenvolvedor Back-end ou Full Stack, nível Júnior/Pleno, nacional ou internacional, remoto ou híbrido.	Terracottocat
O que estou construindo agora
| Produto | O que é | Status | |---|---|---| | **AgendaFlow** | SaaS de agendamento via WhatsApp com atendimento por IA (Claude) | Em produção | | **AgendaFlow Admin** | Painel administrativo com dashboard executivo, operacional e financeiro | Em produção | | **FlowPay** | App Android para clientes acompanharem e pagarem suas mensalidades | Em publicação na Play Store |
Experiência
Fundador e Desenvolvedor · Flow / Nexus Informática (desde 05/2024) Criação e operação de produtos SaaS próprios, do banco de dados ao deploy e à cobrança do cliente. Desenvolvi sozinho o AgendaFlow (FastAPI, PostgreSQL, Claude API, WhatsApp Cloud API), o painel administrativo em Next.js e o app FlowPay em Flutter, com pagamentos via Mercado Pago e Asaas, workers agendados e infraestrutura no Railway. Pela Nexus Informática, também atuo como consultor e técnico de TI para empresas e escritórios: montagem e manutenção de desktops, suporte de hardware e software e gestão direta de clientes.

Desenvolvedor Back-end · Wooba C#, ASP.NET MVC, APIs REST, JavaScript e jQuery em uma plataforma de reservas de viagens em produção. Implementei e depurei fluxos independentes de busca de voos e hotéis, corrigi problemas de roteamento, bugs de sincronização no motor de front-end e falhas de autenticação com fornecedores.

Projetos em destaque
AgendaFlow · SaaS de agendamento via WhatsApp com IA
Python FastAPI PostgreSQL Claude API WhatsApp Railway

Empresas como barbearias, salões e clínicas contratam o AgendaFlow e seus clientes passam a agendar, remarcar e cancelar horários conversando no WhatsApp da própria empresa. O atendimento é feito pelo Claude com tool-use, consultando a agenda real no banco.

IA com ferramentas reais: loop de tool-use com o Claude para listar, criar, cancelar e reagendar horários, com controle de histórico que nunca separa pares tool_use/tool_result
Webhook resiliente: deduplicação por message_id, expiração de conversa e resposta sempre 200 para evitar reenvio em cascata da Meta
Modelo multiunidade: empresas, unidades com número próprio de WhatsApp, profissionais e serviços, com trava de conflito por profissional usando índices parciais
Pagamentos: PIX via Mercado Pago para mensalidades e Asaas com subconta por empresa para sinais de agendamento, webhook de confirmação e estorno automático com camadas de segurança
Segurança: API keys com HMAC + pepper, bcrypt + JWT no painel, validação real de CNPJ e rate limiting distribuído persistido no PostgreSQL
Operação: workers agendados para cobrança e lembretes, score de risco, central de pendências e painel de saúde operacional por empresa
Onboarding via Meta: Cadastro Incorporado (Embedded Signup) para conectar o WhatsApp Business do cliente direto pelo painel
Repositórios: agendaflow-backend · AgendaFlow-Admin

AgendaFlow Admin · Painel administrativo
Next.js TypeScript Tailwind

Painel em Next.js (App Router) para gerenciar empresas, unidades, profissionais, serviços, formas de pagamento e templates de mensagem. O dashboard reúne visão executiva, operacional e financeira, incluindo um motor de preço sugerido calculado a partir do custo real de IA e infraestrutura com margem configurável.

FlowPay · App de cobrança
Flutter Dart Firebase

App Android da Flow para que clientes pagantes acompanhem e paguem suas faturas de qualquer produto Flow. Login por código via WhatsApp, notificações push, atualização em tempo real, token em armazenamento seguro (Keystore) e tratamento completo de perda de conexão. Foi meu primeiro projeto mobile, levado do zero até a publicação.

Repositório: FlowPay

API de Livros · Back-end com observabilidade e CI/CD
FastAPI Celery Kafka Kubernetes

API em FastAPI e SQLAlchemy com stack completa de observabilidade (Celery, Redis, Kafka e ELK com logs em JSON via Logstash), testes com pytest isolados por conftest.py e pipeline no GitHub Actions publicando imagens no GHCR e fazendo deploy em Kubernetes (Minikube) via runner self-hosted.

Repositório: livros-api

Pokémon API · Projeto companheiro
API na mesma arquitetura da API de Livros, com tipos duplos, stats reais da primeira geração, endpoint de batalha e tarefas assíncronas com Celery.

Repositório: pokemon-api

ViajaJá · Portal de viagens
Portal em React.js e TypeScript com arquitetura em Micro Frontends.

Tecnologias
**Back-end** [![Back-end Skills](https://skillicons.dev/icons?i=python,fastapi,cs,dotnet,nodejs,nestjs)](https://skillicons.dev) **Front-end e mobile** [![Front-end Skills](https://skillicons.dev/icons?i=nextjs,react,ts,js,tailwind,flutter,dart)](https://skillicons.dev) **Dados e infraestrutura** [![Data & Infra Skills](https://skillicons.dev/icons?i=postgres,redis,kafka,docker,kubernetes,githubactions,firebase,linux,git)](https://skillicons.dev) **IA e integrações** [![Claude API](https://img.shields.io/badge/Claude_API-D97757?style=for-the-badge&logo=anthropic&logoColor=white)](https://www.anthropic.com) [![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com) [![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com) [![WhatsApp](https://img.shields.io/badge/WhatsApp_Cloud_API-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://developers.facebook.com/docs/whatsapp) [![Mercado Pago](https://img.shields.io/badge/Mercado_Pago-00B1EA?style=for-the-badge&logo=mercadopago&logoColor=white)](https://www.mercadopago.com.br)
Área	Tecnologias
Back-end	Python, FastAPI, psycopg, SQLAlchemy, Celery, C#, ASP.NET, ASP.NET MVC, .NET, Node.js, NestJS
Front-end	Next.js, React.js, TypeScript, JavaScript, Tailwind CSS, HTML5, CSS, jQuery, Vite, Micro Frontends
Mobile	Flutter, Dart, Firebase Cloud Messaging
Dados	PostgreSQL, SQL Server, SQLite, Redis, SQL
Infraestrutura	Docker, Docker Compose, Kubernetes, GitHub Actions, GHCR, Railway, Apache Kafka, ELK Stack
IA	Claude API (tool-use), Claude Code, MCP, OpenAI, LangChain, LLMs locais
Pagamentos e mensageria	Mercado Pago (PIX), Asaas (subcontas), WhatsApp Cloud API, Meta Embedded Signup
Práticas	API REST, webhooks idempotentes, TDD, Clean Architecture, System Design, Git/GitHub, Postman
Formação
Engenharia de Software · FIAP (em andamento)
Desenvolvimento Back-end Python · EBAC (em andamento)
EBAC · Escola Britânica de Artes Criativas e Tecnologia · Desenvolvimento de API, Arquitetura de Software, Integração e Entrega Contínua (CI/CD), Desenvolvimento Back-end, Desenvolvimento Front-end, IA Generativa para Desenvolvedores Web, Programação Orientada a Objetos, Desenvolvimento Orientado a Testes
T.I do Zero ao Pro · Introdução à Programação, Linux
![FIAP](https://img.shields.io/badge/FIAP-Engenharia_de_Software-1a1a2e?style=for-the-badge) ![EBAC](https://img.shields.io/badge/EBAC-Back--end_Python_%26_Full_Stack-1a1a2e?style=for-the-badge) ![T.I do Zero ao Pro](https://img.shields.io/badge/T.I_do_Zero_ao_Pro-Introdução_à_Programação-1a1a2e?style=for-the-badge)
Estudar faz parte da rotina, não é uma etapa concluída. Os próximos alvos são certificações em cloud (AWS/Azure) e inglês profissional.

Trajetória
text 2023 Python, lógica de programação, POO, estruturas de dados 2024 APIs REST, banco de dados relacional, Git avançado 2024 C#, ASP.NET, ASP.NET MVC em produção na Wooba 2024 Fundação da Nexus Informática 2025 Docker, Kubernetes, PostgreSQL, SQL Server, GitHub Actions 2025 IA generativa: Claude API, OpenAI, LangChain 2025 System Design, Clean Architecture, DDD 2026 AgendaFlow em produção: IA + WhatsApp + PIX 2026 Next.js no painel admin, Flutter no app FlowPay 2026 Cloud (AWS/Azure) e inglês profissional em andamento

GitHub
Igor's GitHub Stats Most Used Languages GitHub Streak Contribution Graph GitHub Trophies
Contato
Aberto a oportunidades nacionais e internacionais como desenvolvedor Back-end ou Full Stack. Se você quer conversar sobre uma vaga, um projeto ou trocar ideia sobre IA aplicada a produto, me chama no LinkedIn ou por email.

[![LinkedIn](https://img.shields.io/badge/Contato_via_LinkedIn-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/igor-santos-devzao) [![Email](https://img.shields.io/badge/Igorsantosdevp@gmail.com-ea4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Igorsantosdevp@gmail.com)
IgorSantosD3v · Anápolis, GO · Brazil Footer
