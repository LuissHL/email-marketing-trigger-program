from apiflask import APIFlask
from flask_cors import CORS
from flask import render_template, jsonify
from app.db import db, migrations
from .config import APP_CONFIGS, Config
from app.api.controllers.auth import auth_bp


LOCAL_URL = "http://127.0.0.1:5000"


def create_app():
    app = APIFlask(__name__, **APP_CONFIGS)
    app.config.from_object(Config)

    CORS(
        app,
        origins=[
            LOCAL_URL,
            # PRODUCTION_URL
        ],
    )
    app.json.sort_keys = False
    app.url_map.strict_slashes = False

    @app.get("/")
    def home():
        """Retorna uma mensagem simples para confirmar que a aplicação está funcionando"""
        return jsonify(message="API is running")
    
    # API
    # Auth
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.init_app(app)
        db.create_all()
        # application_client()
        migrations.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
