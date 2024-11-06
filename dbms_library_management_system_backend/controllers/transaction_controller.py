from flask import Blueprint, jsonify, request
from services.transaction_service import add_transaction, get_transaction_by_id, update_transaction, delete_transaction
from models.transaction_model import TransactionModel
transaction_blueprint = Blueprint('transactions', __name__)

# Create a new transaction
@transaction_blueprint.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.json
    new_transaction = add_transaction(data)
    return jsonify(new_transaction.to_dict()), 201

# Get a transaction by ID
@transaction_blueprint.route('/transactions/<transaction_id>', methods=['GET'])
def retrieve_transaction(transaction_id):
    transaction = get_transaction_by_id(transaction_id)
    if transaction:
        return jsonify(transaction), 200
    return jsonify({'message': 'Transaction not found'}), 404

# Update a transaction
@transaction_blueprint.route('/transactions/<transaction_id>', methods=['PUT'])
def modify_transaction(transaction_id):
    data = request.json
    updated_transaction = update_transaction(transaction_id, data)
    if updated_transaction:
        return jsonify(updated_transaction), 200
    return jsonify({'message': 'Transaction not found'}), 404

# Delete a transaction
@transaction_blueprint.route('/transactions/<transaction_id>', methods=['DELETE'])
def remove_transaction(transaction_id):
    deleted_transaction = delete_transaction(transaction_id)
    if deleted_transaction:
        return jsonify({'message': 'Transaction deleted'}), 200
    return jsonify({'message': 'Transaction not found'}), 404