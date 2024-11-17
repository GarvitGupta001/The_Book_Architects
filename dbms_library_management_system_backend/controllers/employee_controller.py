from flask import Blueprint, jsonify, request
from services.employee_service import create_employee, get_employee_by_id, update_employee, delete_employee,  signup_employee, login_employee
from models.employee_model import EmployeeModel 
employee_blueprint = Blueprint('employees', __name__)


@employee_blueprint.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    new_employee = create_employee(data)
    return jsonify(new_employee.to_dict()), 201


@employee_blueprint.route('/employees/<employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if employee:
        return jsonify(employee), 200
    return jsonify({'message': 'Employee not found'}), 404


@employee_blueprint.route('/employees/<employee_id>', methods=['PUT'])
def modify_employee(employee_id):
    data = request.json
    updated_employee = update_employee(employee_id, data)
    if updated_employee:
        return jsonify(updated_employee), 200
    return jsonify({'message': 'Employee not found'}), 404


@employee_blueprint.route('/employees/<employee_id>', methods=['DELETE'])
def remove_employee(employee_id):
    deleted_employee = delete_employee(employee_id)
    if deleted_employee:
        return jsonify({'message': 'Employee deleted'}), 200
    return jsonify({'message': 'Employee not found'}), 404

@employee_blueprint.route('/employees/signup', methods=['POST'])
def signup():

    data = request.json
    if not data.get('employee_id') or not data.get('password'):
        return jsonify({'message': 'Employee ID and password are required'}), 400

    new_employee = signup_employee(data)
    if not new_employee:
        return jsonify({'message': 'Employee ID already exists'}), 400

    return jsonify(new_employee.to_dict()), 201

@employee_blueprint.route('/employees/login', methods=['POST'])
def login():
    data = request.json
    employee_id = data.get('employee_id')
    password = data.get('password')

    if not employee_id or not password:
        return jsonify({'message': 'Employee ID and password are required'}), 400

    employee = login_employee(employee_id, password)
    if not employee:
        return jsonify({'message': 'Invalid credentials'}), 401

    return jsonify({
        'message': 'Login successful',
        'employee': employee.to_dict()
    }), 200