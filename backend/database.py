import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()  # 🔥 Load .env file

db = SQLAlchemy()

def init_db(app):
    SERVER = os.getenv("DB_SERVER")
    DATABASE = os.getenv("DB_NAME")
    USERNAME = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    DRIVER = os.getenv("DB_DRIVER")

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}:1433/{DATABASE}"
        f"?driver={DRIVER.replace(' ', '+')}"
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)