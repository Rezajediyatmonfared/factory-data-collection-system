from flask import Flask
from config import Config
from app.database import init_db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # مقداردهی اولیه دیتابیس در صورت عدم وجود
    init_db()

    # ثبت روت‌ها (به علت جلوگیری از Circular Import، ایمپورت را در این بخش انجام می‌دهیم)
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
