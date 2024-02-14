# potencia-feminina-django-web

## Nessa semana aprendemos sobre:

**O que é um Framework?**
Um framework é uma estrutura ou conjunto de ferramentas, bibliotecas e convenções que fornecem uma base para o desenvolvimento de software. Ele oferece uma maneira padronizada de criar e gerenciar aplicativos, simplificando tarefas comuns e fornecendo um esqueleto ou uma arquitetura inicial para o projeto.
Cada Framework tem um padrão, os mais conhecidos: MVT e MVC

** MVT (Model-View-Template) **
Model: representa os dados e a lógica de negócios da aplicação.
View: responsável por exibir os dados ao usuário.
Template: responsável pela lógica de apresentação e formatação dos dados antes de serem enviados para a View. O Template é uma representação pré-processada da View.
O Template é responsável por preparar os dados que serão exibidos na View, mas não manipula diretamente as interações do usuário.
Django

** MVC (Model-View-Controller) **
Model: representa os dados e a lógica de negócios da aplicação. Isso inclui a manipulação e o processamento de dados.
View: é a camada de apresentação responsável por exibir os dados ao usuário final. Geralmente, consiste na interface do usuário (UI) e na exibição dos dados formatados.
Controller: atua como um intermediário entre o Model e a View. Ele recebe entradas do usuário, manipula as interações do usuário e atualiza o Model conforme necessário. Ele também atualiza a View para refletir as alterações nos dados.
Laravel

### Django

É um framework web gratuito e de código aberto, escrito em Python, que simplifica a criação de soluções web escaláveis.
Ele é rápido, completo, escalonável, seguro, versátil e popular.
Ele possui as seguintes partes:

- Montar páginas (Templates);
- Interagir com diversos bancos de dados (ORM);
- Validar input dos usuários (Forms);
- Controlar acesso (Authorization);
- Gerenciara aplicação (Admin).

** Aula 1: Instalando o ambiente virtual e conhecendo nosso projeto **

- instalar o ambiente virtual: pip install virtualenv
- criar o ambiente virtual: python -m venv [nome do ambiente virtual]
- entrar na pasta criada: cd .\[nome da pasta]\
- ativar o ambiente virtual: .\Scripts\activate

** Aula 2: Instalando o django e iniciando nosso primeiro aplicativo **

- instalar o Django: pip install django
- criar o projeto: django-admin startproject [nome do projeto] .
- rodar e testar funcionamento: python manage.py runserver
- criar um novo aplicativo: python manage.py startapp [nome do app]

Na pasta projeto fica as configurações gerais do sistema.
Na pasta base implementa as funcionalidades específicas do aplicativo.(Cadastro, visualização, etc)

Sempre que cria um novo aplicativo precisamos avisar o projeto que o app foi criado.

** Aula 3: Views **
Parte do código que trabalha com as visualizações.
São responsáveis por processar as requisições dos clientes, executar a lógica de negócios e retornar respostas. Elas formam a camada onde definimos como nossa aplicação deve se comportar em resposta às ações dos usuários. 