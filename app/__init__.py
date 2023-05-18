from flask import Flask


def create_app():
    app = Flask(__name__)
    app.debug = True

    from .main import login_blueprint, password_blueprint, dashboard_blueprint, logout_blueprint
    app.register_blueprint(login_blueprint)
    app.register_blueprint(password_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(logout_blueprint)

    return app
