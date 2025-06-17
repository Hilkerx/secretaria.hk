Instalação
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto
Crie o ambiente virtual (opcional, mas recomendado):

nginx
Copiar
Editar
python -m venv venv
Ative o ambiente:

No Windows:

Copiar
Editar
venv\Scripts\activate
No Linux/Mac:

bash
Copiar
Editar
source venv/bin/activate
Instale as bibliotecas:

nginx
Copiar
Editar
pip install -r requirements.txt
Aplique as migrações para criar as tabelas do banco:

nginx
Copiar
Editar
python manage.py migrate
Crie um usuário administrador:

nginx
Copiar
Editar
python manage.py createsuperuser
Execute o sistema:

nginx
Copiar
Editar
python manage.py runserver
Abra o navegador e acesse: http://127.0.0.1:8000

Funcionalidades
O sistema inclui:

Autenticação e controle de acesso

Cadastros completos de alunos, professores, disciplinas, notas, contratos e calendários

Edição e exclusão de registros

Interface web simples, com formulários validados

Banco de dados integrado via Django ORM

Segurança com proteção contra requisições não autorizadas (CSRF)

Estrutura e organização
O código segue a divisão padrão do Django:

models.py para definição das tabelas

views.py para as lógicas de exibição

Templates separados por funcionalidade

Comentários explicativos nas funções principais

URLs organizadas por app

Testes realizados
Login e logout com validação de acesso

Cadastro e edição de estudantes e professores

Lançamento e visualização de notas

Verificação de páginas protegidas para usuários não autenticados

Publicação em ambiente externo
Para rodar o sistema em produção, recomenda-se:

Desativar o modo de debug no arquivo settings.py (DEBUG = False)

Definir domínios seguros no ALLOWED_HOSTS

Utilizar servidores como Gunicorn (backend) e Nginx (proxy)

Substituir SQLite por PostgreSQL para maior robustez

Tecnologias usadas
Python 3

Django

SQLite

HTML/CSS

Sobre este documento
Este guia descreve os passos necessários para instalação, configuração, uso e testes da aplicação. O projeto foi desenvolvido como parte de uma atividade acadêmica com prazo final em 18/06. A entrega deve ser feita por meio do envio do link do repositório no GitHub.