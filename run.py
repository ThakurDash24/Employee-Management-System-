from app import create_app, db  # Import the create_app function and the SQLAlchemy instance from the app module

app = create_app()  # Create an instance of the Flask application using the factory function

if __name__ == '__main__':
    with app.app_context():  # Ensure that the app context is available for database operations
        db.create_all()  # Create all tables in the database based on the defined models
    app.run(debug=True)  # Run the Flask application with debug mode enabled
