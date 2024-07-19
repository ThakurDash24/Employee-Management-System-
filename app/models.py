from app import db  # Import the SQLAlchemy instance from the app module

# Define the Employee model class
class Employee(db.Model):
    # Define the table name in the database (optional, defaults to class name)
    __tablename__ = 'employees'
    
    # Define the columns for the Employee table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column with auto-incrementing integer
    name = db.Column(db.String(50), nullable=False)  # Column for employee's name, cannot be null
    position = db.Column(db.String(50), nullable=False)  # Column for employee's position, cannot be null
    salary = db.Column(db.Float, nullable=False)  # Column for employee's salary, cannot be null

    # Method to convert the Employee instance to a dictionary
    def to_dict(self):
        return {
            'id': self.id,  # Employee ID
            'name': self.name,  # Employee name
            'position': self.position,  # Employee position
            'salary': self.salary  # Employee salary
        }
