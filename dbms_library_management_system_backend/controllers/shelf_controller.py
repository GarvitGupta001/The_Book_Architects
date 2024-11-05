from flask import Blueprint, jsonify, request
from services.shelf_service import create_shelf, get_shelf_by_id, update_shelf, delete_shelf
from models.shelf_model import ShelfModel
shelf_blueprint = Blueprint('shelves', __name__)

# Create a new shelf
@shelf_blueprint.route('/shelves', methods=['POST'])
def add_shelf():
    data = request.json
    new_shelf = create_shelf(data)
    return jsonify(new_shelf.to_dict()), 201

# Get shelf by ID
@shelf_blueprint.route('/shelves/<shelf_id>', methods=['GET'])
def get_shelf(shelf_id):
    shelf = get_shelf_by_id(shelf_id)
    if shelf:
        return jsonify(shelf), 200
    return jsonify({'message': 'Shelf not found'}), 404

# Update shelf
@shelf_blueprint.route('/shelves/<shelf_id>', methods=['PUT'])
def modify_shelf(shelf_id):
    data = request.json
    updated_shelf = update_shelf(shelf_id, data)
    if updated_shelf:
        return jsonify(updated_shelf), 200
    return jsonify({'message': 'Shelf not found'}), 404

# Delete shelf
@shelf_blueprint.route('/shelves/<shelf_id>', methods=['DELETE'])
def remove_shelf(shelf_id):
    deleted_shelf = delete_shelf(shelf_id)
    if deleted_shelf:
        return jsonify({'message': 'Shelf deleted'}), 200
    return jsonify({'message': 'Shelf not found'}), 404
