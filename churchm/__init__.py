from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    # ORM
    # database 초기화 'falsk db init'
    # database
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # 블루 프린트
    from .views import main_views, member_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(member_views.bp)

    return app
