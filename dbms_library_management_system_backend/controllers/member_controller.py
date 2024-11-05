from flask import Blueprint, jsonify, request
from services.member_service import create_member, get_member_by_id, update_member, delete_member
from models.member_model import MemberModel
member_blueprint = Blueprint('members', __name__)

# Create a new member
@member_blueprint.route('/members', methods=['POST'])
def add_member():
    data = request.json
    new_member = create_member(data)
    return jsonify(new_member.to_dict()), 201

# Get member by ID
@member_blueprint.route('/members/<member_id>', methods=['GET'])
def get_member(member_id):
    member = get_member_by_id(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({'message': 'Member not found'}), 404

# Update member
@member_blueprint.route('/members/<member_id>', methods=['PUT'])
def modify_member(member_id):
    data = request.json
    updated_member = update_member(member_id, data)
    if updated_member:
        return jsonify(updated_member), 200
    return jsonify({'message': 'Member not found'}), 404

# Delete member
@member_blueprint.route('/members/<member_id>', methods=['DELETE'])
def remove_member(member_id):
    deleted_member = delete_member(member_id)
    if deleted_member:
        return jsonify({'message': 'Member deleted'}), 200
    return jsonify({'message': 'Member not found'}), 404
