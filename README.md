# potencia-feminina-django-web

## SEMANA 07: Django Web

**O que é um Framework?** <br>
Um framework é uma estrutura ou conjunto de ferramentas, bibliotecas e convenções que fornecem uma base para o desenvolvimento de software. Ele oferece uma maneira padronizada de criar e gerenciar aplicativos, simplificando tarefas comuns e fornecendo um esqueleto ou uma arquitetura inicial para o projeto.
Cada Framework tem um padrão, os mais conhecidos: MVT e MVC

**MVT (Model-View-Template)**<br>
Model: representa os dados e a lógica de negócios da aplicação.
View: responsável por exibir os dados ao usuário.
Template: responsável pela lógica de apresentação e formatação dos dados antes de serem enviados para a View. O Template é uma representação pré-processada da View.
O Template é responsável por preparar os dados que serão exibidos na View, mas não manipula diretamente as interações do usuário.
Django

**MVC (Model-View-Controller)** <br>
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

**Aula 1: Instalando o ambiente virtual e conhecendo nosso projeto** ⚠️

- instalar o ambiente virtual: pip install virtualenv
- criar o ambiente virtual: python -m venv [nome do ambiente virtual]
- entrar na pasta criada: cd .\[nome da pasta]\
- ativar o ambiente virtual: .\Scripts\activate

**Aula 2: Instalando o django e iniciando nosso primeiro aplicativo** ⚠️

- instalar o Django: pip install django
- criar o projeto: django-admin startproject [nome do projeto] .
- rodar e testar funcionamento: python manage.py runserver
- criar um novo aplicativo: python manage.py startapp [nome do app]

Na pasta projeto fica as configurações gerais do sistema.
Na pasta base implementa as funcionalidades específicas do aplicativo.(Cadastro, visualização, etc)

Sempre que cria um novo aplicativo precisamos avisar o projeto que o app foi criado.
- registrar no settings.py

**Aula 3: Views** 📕✏️<br>
Parte do código que trabalha com as visualizações.
São responsáveis por processar as requisições dos clientes, executar a lógica de negócios e retornar respostas. Elas formam a camada onde definimos como nossa aplicação deve se comportar em resposta às ações dos usuários. 

**Aula 4: URLs** 📕✏️<br>
HttpResponse responsável pela comunicação pela internet.
Para as Views acessarem as páginas, elas precisam de uma url.
As URLs no Django são responsáveis por mapear os endereços da web para funções de visualização em sua aplicação. Elas definem como as requisições do navegador devem ser tratadas e quais respostas devem ser retornadas. 

**Aula 5 e 6: Template parte 1 e 2** 📕✏️<br>
Os templates no Django são arquivos que definem a aparência e o layout das suas páginas da web. Eles permitem que você insira dados dinâmicos em páginas HTML, tornando-as interativas e personalizáveis.<br>
Os arquivos estáticos são recursos como imagens, folhas de estilo CSS e arquivos JavaScript que são servidos diretamente para o navegador, sem processamento dinâmico. 
Tudo que for JS e CSS, ficam na pasta static. Nesse projeto usamos o framework bootstrap para estilizar nossa página.

- pip install django-bootstrap-v5
- registrar no settings.py

**Aula 7: Forms** 📕✏️<br>
Parte essencial para coletar informações dos usuários em aplicativos da web. Eles permitem que você defina campos de formulário, regras de validação e renderização de formulários em templates de maneira simples e eficiente.
O Forms é dividido nas seguintes partes:
- Classe: ela especifica os campos no formulário, seu layout, exibe widgets, rótulos, valores iniciais, valores válidos e mensagens de erro associadas a campos inválidos.
- Campos (Fields): os campos definem os tipos de dados que você deseja coletar do usuário (por exemplo, texto, número, data, etc.). Existem vários tipos de campos, como CharField, IntegerField, DateField, etc.
- Widgets: controlam a renderização dos campos no HTML. Por exemplo, um campo CharField pode ser renderizado como uma caixa de texto ou um campo de senha.
- Validação: o Django realiza a validação automática dos dados enviados pelo usuário com base nas regras definidas nos campos. Se os dados não forem válidos, o formulário exibirá mensagens de erro.
- Renderização de Templates: os formulários são renderizados em templates HTML usando a tag {% form %}. Você pode personalizar a aparência do formulário no template.

**Aula 8: Models e ModelForm** 📕✏️<br>
São partes essenciais do Django para trabalhar com bancos de dados e formulários.

1. Models:
  - Os models no Django são classes Python que definem a estrutura dos dados que serão armazenados no banco de dados.
  - Cada model representa uma tabela no banco de dados e seus campos correspondem às colunas dessa tabela.
  - Os models incluem informações como tipos de campo, relacionamentos (chaves estrangeiras, chaves primárias) e métodos para interagir com os dados.
2. ModelForms:
  - Os ModelForms são uma extensão dos Forms padrão do Django.
  - Eles são criados automaticamente com base em um model existente.
  - Um ModelForm mapeia os campos do model para campos de formulário, permitindo que você crie formulários facilmente para adicionar, editar ou exibir dados do banco de dados.
  - Eles também incluem validação automática com base nas regras definidas nos models.

  Instalar um extensão para conseguir visualizar o banco de dados no VSCode. SQLite Viewer

  Sempre que houver uma atualização no banco de dados, deve rodar esses  comando de imigração.
  - Gerar um arquivo que deve ser enviado para o banco: python manage.py makemigrations
  - Envia para o banco: python manage.py migrate
  - Ir na views e incluir a conexão com o banco.

**Aula 9: Filtros, buscas e admin** 📕✏️<br>
- Filtros: você pode filtrar registros de um modelo com base em condições específicas. Por exemplo, obter todos os eventos com o campo “ano” menor que 2018.
- Buscas: o módulo Admin permite adicionar filtros a campos de modelo para facilitar a pesquisa e a navegação. Você pode definir os campos que deseja filtrar usando list_filter no arquivo admin.py.
- Módulo Admin: é uma parte essencial do Django que permite gerenciar seus dados de forma visual. Principais recursos: lista de objetos, formulários de edição, filtros e pesquisa, ações em lote e personalização de visualização.

Explorando o admin:
- Instalar: python manage.py createsuperuser
    1. Definir username
    2. Definir email
    3. Definir senha
    4. Senha novamente

## SEMANA 8: Django ORM

**Aula 1: Manipulando bases de dados parte 1** 📕✏️<br>
- criar nova aplicação python manage.py startapp [nome do app]
- adicionar nova aplicação no settings
- criar a model
- python manage.py makemigrations (sempre que faz alteração no banco de dados)
- python manage.py migrate (sempre que roda o makemigrations)

**Aula 2: Manipulando bases de dados parte 2** 📕✏️<br>
- criar novo forms no banco cursos
- atualizar view, forms
- criar arquivo urls e atualizar urls geral

**Aula 3: Validação de Dados** 📕✏️<br>
- dentro de forms implementar um def para validação.

**Aula 4: Utilizando Cache na aplicação** 📕✏️<br>

O cache é uma técnica para melhorar o desempenho e a eficiência de aplicações e sistemas. 
Vantagens: velocidade de acesso, redução do consumo de recursos, diminuição da latência, alívio da rede e melhoria na experiência do usuário.

🔗 [Django Documentation](https://docs.djangoproject.com/en/5.0/)

O que iremos utilizar o Redis: é uma ferramenta _key-value_ frequentemente integrada em projetos Django para otimizar desempenho e eficiência. Ele é utilizado como cache para armazenar dados frequentemente acessados, como resultados de consultas ao banco de dados, reduzindo latência e melhorando tempo de resposta. Além disso, o Redis é empregado para armazenar sessões de usuários, permitindo a manutenção do estado entre solicitações HTTP, e também na gestão de filas e tarefas em segundo plano, como envio de e-mails, garantindo eficiência e escalabilidade. Em recursos em tempo real, como o Django Channels, o Redis atua como uma camada de armazenamento para nomes de canais e grupos, viabilizando a comunicação entre diferentes instâncias de consumidores de forma instantânea.