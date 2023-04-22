from flask import Flask


def create_app():
    app = Flask(__name__)
    #app.config['SECRET_KEY'] = SECRET_KEY
    #app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    #app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
    #app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    

    from .blueprints.uberapp import app_bp
    app.register_blueprint(app_bp)
    return app
