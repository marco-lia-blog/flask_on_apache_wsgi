"""Initialize app."""
from flask import Flask

def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)


    with app.app_context():
        from . import routes

        # Register Blueprints
        app.register_blueprint(routes.main_bp)

        return app
