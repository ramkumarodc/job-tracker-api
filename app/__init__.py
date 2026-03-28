from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes import jobs_bp
    app.register_blueprint(jobs_bp)

    return app
