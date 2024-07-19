from flask import Flask  # Import the Flask class to create the application instance
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy for database management
from .config import Config  # Import configuration settings

# Create an instance of SQLAlchemy to handle database interactions
db = SQLAlchemy()

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Load configuration from the Config class
    app.config.from_object(Config)

    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)

    # Set up the application context to register Blueprints and models
    with app.app_context():
        # Import the Blueprint for handling main routes
        from .routes import main as main_blueprint
        # Register the main Blueprint with the app
        app.register_blueprint(main_blueprint)
        
        # Import the Blueprint for handling error routes
        from .error import error as error_blueprint
        # Register the error Blueprint with the app
        app.register_blueprint(error_blueprint)
        
        # Import the models to ensure they are registered with SQLAlchemy
        from . import models

    # Return the Flask application instance
    return app
