# 📌 Projeto Django - Cadastro e Geração de PDF

Este é um projeto Django para **cadastro de pessoas carentes** em um programa social, com a capacidade de gerar um **arquivo PDF** contendo as informações registradas.

## 📋 Funcionalidades
- 📑 **Cadastro de Usuários** com informações detalhadas
- 🔍 **Gerenciamento de Inscrições** com visualização e edição de dados
- 🔐 **Armazenamento Seguro** das informações coletadas
- 🖨️ **Geração de PDF** com os dados do usuário
- 📡 **Modo Offline** para preenchimento de formulários sem internet

## 🛠️ Tecnologias Utilizadas
- **Django 5.1.5** (Back-end)
- **MySQL** (Banco de Dados)
- **ReportLab** (Geração de PDFs)
- **JavaScript** (Formulários offline)
- **HTML/CSS** (Interface Web)

## 📦 Instalação
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure o arquivo `.env` com as credenciais do banco de dados:
   ```sh
   DB_NAME=seu_banco
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   ```

4. Execute as migrações do banco de dados:
   ```sh
   python manage.py migrate
   ```

5. Inicie o servidor Django:
   ```sh
   python manage.py runserver
   ```

## 📜 Requisitos
- `asgiref==3.8.1`
- `chardet==5.2.0`
- `Django==5.1.5`
- `dotenv==0.9.9`
- `mysqlclient==2.2.7`
- `pillow==11.1.0`
- `python-dotenv==1.0.1`
- `reportlab==4.2.5`
- `sqlparse==0.5.3`
- `tzdata==2025.1`

## 🎯 Objetivo
Este projeto foi desenvolvido para facilitar o cadastro de pessoas carentes para um **programa social do governo**, garantindo a privacidade dos dados e a acessibilidade do sistema.

## 🏗️ Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** e enviar **pull requests**.
