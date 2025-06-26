# project4-2025a-joao-matheus-isaac

Projeto desenvolvido para a disciplina de [Desenvolvimento de Software para a Web](http://github.com/andreainfufsm/elc1090-2025a) — 2025a, utilizando o framework Django.

Link de acesso ao site: [https://yucky-noreen-sou-aluno-2ab614ec.koyeb.app](https://yucky-noreen-sou-aluno-2ab614ec.koyeb.app)

---

## Descrição

Este projeto faz uso de um banco de dados remoto para criação e armazenamento de lutadores e golpes associados a estes lutadores, utilizando de usuários separados, um limite de 2 lutadores por usuário, registro, login com gmail, geração de imagens de lutadores com IA e atualmente um teste do multiplayer com pareamento em tempo real, não finalizado para ter gameplay real, o objetivo final do projeto sendo a integração com a gameplay.

---

## Desenvolvedores

- João Marcos – Sistemas de Informação  
- Matheus – Sistemas de Informação  
- Isaac – Sistemas para Internet  

---

## Tecnologias Utilizadas

- Python  
- Django (Channels)
- HTML  
- CSS  
- JavaScript  
- Supabase (PostgreSQL) (Buckets)
- Koyeb (Deploy)
- Redis (Message Broker dos websockets)
- Gunicorn (pro deploy)
- Daphne (pro deploy com webscokets)
- Modelo de IA "black-forest-labs/FLUX.1-dev" do Huggingface
- Async (mesmo que django naturalmente não seja)

---

## Ferramentas de Desenvolvimento

- Visual Studio Code  
- GitHub  
- Pixlr (para criação de logo e imagens)  

---

## Requisitos (direto do requirements.txt)

- ﻿Django==5.2.1
- channels==4.2.2
- channels_redis==4.2.1
- asgiref==3.8.1
- daphne==4.2.0
- redis==6.2.0
- python-dotenv==1.1.0
- requests==2.32.4
- supabase==2.16.0
- gunicorn==23.0.0
- whitenoise==6.9.0
- tzdata==2025.2
- psycopg2-binary==2.9.10 

---

## Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e executar o projeto em sua máquina:

---

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

---

### 2. Criar um Ambiente Virtual

```bash
python -m venv venv
venv\Scripts\activate     # Para Windows
```

---

### 3. Instalar as Dependências

Instale os pacotes necessários com base no arquivo `requirements.txt` localizado dentro da pasta `projeto_lutadores`:

```bash
pip install -r requirements.txt
```

---

### 4. Configurar Tokens de Acesso

Você precisará obter os seguintes tokens:

- Token de API do Hugging Face com permissões de acesso às APIs de inferência.
- Credenciais do Google Auth.
- Token de acesso Supabase
- Token de acesso Redis

Só precisa criar um .env na raiz do projeto com esses tokens. O problema mesmo vai ser precisar criar 4 contas diferentes em lugares separados

---

### 5. Executar a Aplicação

Com o ambiente configurado corretamente, execute o seguinte comando para iniciar o servidor com suporte a WebSockets:

```bash
daphne projeto_lutadores.asgi:application
```

---

O projeto estará então disponível para uso local.

