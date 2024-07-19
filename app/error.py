from flask import Blueprint, jsonify

# Create a Blueprint for handling errors
error = Blueprint('error', __name__)

# Handler for 404 Not Found errors
@error.app_errorhandler(404)
def not_found_error(error):
    # Return a JSON response with a 404 status code
    return jsonify({'message': 'Resource not found'}), 404

# Handler for 500 Internal Server errors
@error.app_errorhandler(500)
def internal_error(error):
    # Return a JSON response with a 500 status code
    return jsonify({'message': 'Internal server error'}), 500

# Handler for 400 Bad Request errors
@error.app_errorhandler(400)
def bad_request_error(error):
    # Return a JSON response with a 400 status code
    return jsonify({'message': 'Bad request'}), 400

# Handler for 403 Forbidden errors
@error.app_errorhandler(403)
def forbidden_error(error):
    # Return a JSON response with a 403 status code
    return jsonify({'message': 'Forbidden access'}), 403

# Handler for 401 Unauthorized errors
@error.app_errorhandler(401)
def unauthorized_error(error):
    # Return a JSON response with a 401 status code
    return jsonify({'message': 'Unauthorized access'}), 401
