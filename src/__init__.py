"""Base module, create_app (application factory) can be called by a WSGI like Gunicorn."""
from flask import Flask 

def create_app():
    app = Flask(__name__)
    from src.routes.default import default
    app.register_blueprint(default)
    from src.routes.predict import predict
    app.register_blueprint(predict)
    return app
