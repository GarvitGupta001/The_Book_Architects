from flask import Blueprint, jsonify, request
from services.publisher_service import create_publisher, get_publisher_by_id, update_publisher, delete_publisher
from models.publisher_model import PublisherModel
publisher_blueprint = Blueprint('publishers', __name__)

# Create a new publisher
@publisher_blueprint.route('/publishers', methods=['POST'])
def add_publisher():
    data = request.json
    new_publisher = create_publisher(data)
    return jsonify(new_publisher.to_dict()), 201

# Get publisher by ID
@publisher_blueprint.route('/publishers/<publisher_id>', methods=['GET'])
def get_publisher(publisher_id):
    publisher = get_publisher_by_id(publisher_id)
    if publisher:
        return jsonify(publisher), 200
    return jsonify({'message': 'Publisher not found'}), 404

# Update publisher
@publisher_blueprint.route('/publishers/<publisher_id>', methods=['PUT'])
def modify_publisher(publisher_id):
    data = request.json
    updated_publisher = update_publisher(publisher_id, data)
    if updated_publisher:
        return jsonify(updated_publisher), 200
    return jsonify({'message': 'Publisher not found'}), 404

# Delete publisher
@publisher_blueprint.route('/publishers/<publisher_id>', methods=['DELETE'])
def remove_publisher(publisher_id):
    deleted_publisher = delete_publisher(publisher_id)
    if deleted_publisher:
        return jsonify({'message': 'Publisher deleted'}), 200
    return jsonify({'message': 'Publisher not found'}), 404
