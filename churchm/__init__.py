from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import MetaData

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

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
    from .views import main_views, member_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(member_views.bp)
    app.register_blueprint(auth_views.bp)

    if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)

    return app
