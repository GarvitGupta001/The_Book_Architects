from flask import Blueprint, jsonify, request
from services.transaction_service import add_transaction, get_transaction_by_id, update_transaction, delete_transaction, get_books_issued_by_member, get_books_due_soon
from models.transaction_model import TransactionModel
from services.fine_service import calculate_and_store_fine

transaction_blueprint = Blueprint('transactions', __name__)



@transaction_blueprint.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.json
    new_transaction = add_transaction(data)
    if data.get('return_date'):
        # If return_date is provided, calculate the fine
        fine_result = calculate_and_store_fine(new_transaction.transaction_id)
        new_transaction.fine = fine_result  # Include fine details in the response

    return jsonify(new_transaction.to_dict()), 201


@transaction_blueprint.route('/transactions/<transaction_id>', methods=['GET'])
def retrieve_transaction(transaction_id):
    transaction = get_transaction_by_id(transaction_id)
    if transaction:
        return jsonify(transaction), 200
    return jsonify({'message': 'Transaction not found'}), 404


@transaction_blueprint.route('/transactions/<transaction_id>', methods=['PUT'])
def modify_transaction(transaction_id):
    data = request.json
    updated_transaction = update_transaction(transaction_id, data)
    if updated_transaction:
        return jsonify(updated_transaction), 200
    return jsonify({'message': 'Transaction not found'}), 404


@transaction_blueprint.route('/transactions/<transaction_id>', methods=['DELETE'])
def remove_transaction(transaction_id):
    deleted_transaction = delete_transaction(transaction_id)
    if deleted_transaction:
        return jsonify({'message': 'Transaction deleted'}), 200
    return jsonify({'message': 'Transaction not found'}), 404


@transaction_blueprint.route('/issued_books/<member_id>', methods=['GET'])
def list_books_issued_by_member(member_id):
    books = get_books_issued_by_member(member_id)
    
    if books:
        return jsonify(books), 200
    return jsonify({'message': 'No books issued by this member.'}), 404


@transaction_blueprint.route('/books/due_soon', methods=['GET'])
def list_books_due_soon():
    due_soon_books = get_books_due_soon()
    if due_soon_books:
        return jsonify(due_soon_books), 200
    return jsonify({'message': 'No books are due soon.'}), 404

