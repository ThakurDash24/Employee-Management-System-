class Config:
    # Database URI configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # URI for the SQLite database. 
    # The 'sqlite:///site.db' indicates that the SQLite database file is named 'site.db' and located in the same directory as the application.

    # Disable modification tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disables Flask-SQLAlchemy's modification tracking. 
    # This reduces overhead as it's not required for most applications. 
    # Setting this to False is recommended to avoid unnecessary performance costs.
