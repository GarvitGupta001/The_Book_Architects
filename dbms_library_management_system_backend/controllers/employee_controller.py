from flask import Blueprint, jsonify, request
from services.employee_service import create_employee, get_employee_by_id, update_employee, delete_employee
from models.employee_model import EmployeeModel 
employee_blueprint = Blueprint('employees', __name__)

# Create employee
@employee_blueprint.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    new_employee = create_employee(data)
    return jsonify(new_employee.to_dict()), 201

# Get employee by ID
@employee_blueprint.route('/employees/<employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if employee:
        return jsonify(employee), 200
    return jsonify({'message': 'Employee not found'}), 404

# Update employee
@employee_blueprint.route('/employees/<employee_id>', methods=['PUT'])
def modify_employee(employee_id):
    data = request.json
    updated_employee = update_employee(employee_id, data)
    if updated_employee:
        return jsonify(updated_employee), 200
    return jsonify({'message': 'Employee not found'}), 404

# Delete employee
@employee_blueprint.route('/employees/<employee_id>', methods=['DELETE'])
def remove_employee(employee_id):
    deleted_employee = delete_employee(employee_id)
    if deleted_employee:
        return jsonify({'message': 'Employee deleted'}), 200
    return jsonify({'message': 'Employee not found'}), 404
