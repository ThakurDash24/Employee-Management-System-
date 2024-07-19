from flask import Blueprint, request, jsonify  # Import Flask utilities for routing and JSON handling
from app import db  # Import the SQLAlchemy instance
from .models import Employee  # Import the Employee model

# Create a new Blueprint for handling routes
main = Blueprint('main', __name__)

# Define the route for the home page
@main.route('/')
def home():
    return "WELCOME TO THE EMPLOYEE MANAGEMENT SYSTEM"

# Define the route for creating a new employee
@main.route('/employee', methods=['POST'])
def create_employee():
    # Get the JSON data from the request
    data = request.get_json()

    # Create a new Employee instance with the data
    new_emp = Employee(name=data['name'], position=data['position'], salary=data['salary'])

    # Add the new employee to the database session and commit
    db.session.add(new_emp)
    db.session.commit()

    # Return the newly created employee data as JSON with a 201 status code
    return jsonify(new_emp.to_dict()), 201

# Define the route for retrieving an employee by ID
@main.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    # Query the database for the employee by ID
    employee = Employee.query.get(employee_id)

    # If the employee is not found, return a 404 error with a message
    if not employee:
        return jsonify({'message': f"Employee with id {employee_id} not found!"}), 404

    # Return the employee data as JSON
    return jsonify(employee.to_dict())

# Define the route for updating an employee by ID
@main.route('/employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    # Query the database for the employee by ID
    employee = Employee.query.get(employee_id)

    # If the employee is not found, return a 404 error with a message
    if not employee:
        return jsonify({'message': "Employee not found"}), 404

    # Get the updated data from the request
    data = request.get_json()
    employee.name = data['name']
    employee.position = data['position']
    employee.salary = data['salary']

    # Commit the updated employee data to the database
    db.session.commit()

    # Return a success message as JSON
    return jsonify({'message': "Employee updated successfully"})

# Define the route for deleting an employee by ID
@main.route('/employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    # Query the database for the employee by ID
    employee = Employee.query.get(employee_id)

    # If the employee is not found, return a 404 error with a message
    if not employee:
        return jsonify({'message': "Employee not found"}), 404

    # Delete the employee from the database session and commit
    db.session.delete(employee)
    db.session.commit()

    # Return a success message as JSON
    return jsonify({'message': "Employee deleted successfully"})
