# Controle de Estoque de Eletrodomésticos

Este projeto é um sistema simples de controle de estoque de eletrodomésticos, composto por uma API em Flask (Python) e uma SPA (Single Page Application) com HTML, CSS e JavaScript. O sistema permite cadastrar, listar, buscar e excluir produtos no estoque, oferecendo uma documentação interativa via Swagger.


#  Tecnologias Utilizadas

- Python 3
- Flask
- SQLite
- Flask-SQLAlchemy
- Flask-Swagger (ou flasgger)
- HTML, CSS e JavaScript (SPA)


# Instruções de Instalação (API)

# 1. Clone o repositório da API

# 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
```

# 3. Ative o ambiente virtual

- Windows:
  ```bash
  venv\Scripts\activate
  ```

- Linux/macOS:
  ```bash
  source venv/bin/activate
  ```

# 4. Instale as dependências

```bash
pip install -r requirements.txt
```

# 5. Inicie a aplicação

```bash
flask run
```

Acesse a API no navegador:  
`http://localhost:5000`

Acesse a documentação Swagger:  
`http://localhost:5000/api/docs`


