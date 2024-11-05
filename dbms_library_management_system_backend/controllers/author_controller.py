from flask import Blueprint, jsonify, request
from services.author_service import create_author, get_author_by_id, update_author, delete_author
from models.author_model import AuthorModel
author_blueprint = Blueprint('authors', __name__)

# Create author
@author_blueprint.route('/authors', methods=['POST'])
def add_author():
    data = request.json
    new_author = create_author(
        author_id=data.get('author_id'),
        author_name=data.get('author_name'),
        author_dob=data.get('author_dob'),
        author_origin=data.get('author_origin'),
        about=data.get('about')
    )
    return jsonify(new_author.to_dict()), 201

# Get author by ID
@author_blueprint.route('/authors/<author_id>', methods=['GET'])
def get_author(author_id):
    author = get_author_by_id(author_id)
    if author:
        return jsonify(author), 200
    return jsonify({'message': 'Author not found'}), 404

# Update author
@author_blueprint.route('/authors/<author_id>', methods=['PUT'])
def modify_author(author_id):
    data = request.json
    updated_author = update_author(
        author_id,
        author_name=data.get('author_name'),
        author_dob=data.get('author_dob'),
        author_origin=data.get('author_origin'),
        about=data.get('about')
    )
    if updated_author:
        return jsonify(updated_author), 200
    return jsonify({'message': 'Author not found'}), 404

# Delete author
@author_blueprint.route('/authors/<author_id>', methods=['DELETE'])
def remove_author(author_id):
    deleted_author = delete_author(author_id)
    if deleted_author:
        return jsonify({'message': 'Author deleted'}), 200
    return jsonify({'message': 'Author not found'}), 404