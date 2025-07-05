from app import create_app

# Cria a instância da aplicação usando a factory function
app = create_app()

if __name__ == '__main__':
    # Executa a aplicação
    app.run(debug=True, port=5000)
