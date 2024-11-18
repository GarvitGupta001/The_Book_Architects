from flask import Blueprint, jsonify, request
from services.fine_service import create_fine, get_fine_by_id, update_fine, delete_fine
from models.fine_model import FineModel
from services.fine_service import calculate_and_store_fine
fine_blueprint = Blueprint('fines', __name__)


@fine_blueprint.route('/fines', methods=['POST'])
def add_fine():
    data = request.json
    new_fine = create_fine(data)
    return jsonify(new_fine.to_dict()), 201


@fine_blueprint.route('/fines/<fine_id>', methods=['GET'])
def get_fine(fine_id):
    fine = get_fine_by_id(fine_id)
    if fine:
        return jsonify(fine), 200
    return jsonify({'message': 'Fine not found'}), 404


@fine_blueprint.route('/fines/<fine_id>', methods=['PUT'])
def modify_fine(fine_id):
    data = request.json
    updated_fine = update_fine(fine_id, data)
    if updated_fine:
        return jsonify(updated_fine), 200
    return jsonify({'message': 'Fine not found'}), 404


@fine_blueprint.route('/fines/<fine_id>', methods=['DELETE'])
def remove_fine(fine_id):
    deleted_fine = delete_fine(fine_id)
    if deleted_fine:
        return jsonify({'message': 'Fine deleted'}), 200
    return jsonify({'message': 'Fine not found'}), 404



@fine_blueprint.route('/fines/<transaction_id>', methods=['GET'])
def calculate_fine(transaction_id):
    
    result = calculate_and_store_fine(transaction_id)
    if 'error' in result:
        return jsonify({'message': result['error']}), 404
    return jsonify(result), 200
