from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
import os

def create_app():

    app = Flask(__name__, static_folder='../static')
    CORS(app)

    # Garante que o diretório de instância exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import database
    with app.app_context():
        database.init_db()

    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json' 
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "API de Controle de Estoque Estruturada"}
    )
    app.register_blueprint(swaggerui_blueprint)

    from . import routes
    app.register_blueprint(routes.bp)

    return app
