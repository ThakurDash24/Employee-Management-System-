from flask import Flask  # Import Flask class to create the application
from config import Config  # Import configuration settings from the Config class
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy for database operations

# Initialize SQLAlchemy object
db = SQLAlchemy()

def create_app():
    # Create a new Flask application instance
    app = Flask(__name__)

    # Load configuration settings from Config class
    app.config.from_object(Config)

    # Initialize SQLAlchemy with the app instance
    db.init_app(app)

    # Use application context to set up routes and models
    with app.app_context():
        # Import routes and register the blueprint for route handling
        from .routes import main as main_blueprint
        app.register_blueprint(main_blueprint)

        # Import models to ensure they are registered with SQLAlchemy
        from . import models
    
    # Return the configured Flask application instance
    return app
