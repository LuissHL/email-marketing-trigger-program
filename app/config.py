import os
import dotenv
import pymysql


pymysql.install_as_MySQLdb()

dotenv.load_dotenv()

APP_CONFIGS = {
    "title": "Email Marketing",
    # "template_folder": "app/static/templates",
    # "static_folder": 'controllers/web/static',
    "docs_path": "/api/docs",
}


class Config:
    CORS_HEADERS = "Access-Control-Allow-Origin"
    JSON_SORT_KEYS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SERVERS = [{"name": "Dev Server", "url": "http://127.0.0.1:5000"}]
