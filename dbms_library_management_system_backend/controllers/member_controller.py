from flask import Blueprint, jsonify, request
from services.member_service import create_member, get_member_by_id, update_member, delete_member,signup_member, login_member
from models.member_model import MemberModel
member_blueprint = Blueprint('members', __name__)


@member_blueprint.route('/members', methods=['POST'])
def add_member():
    data = request.json
    new_member = create_member(data)
    return jsonify(new_member.to_dict()), 201


@member_blueprint.route('/members/<member_id>', methods=['GET'])
def get_member(member_id):
    member = get_member_by_id(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({'message': 'Member not found'}), 404


@member_blueprint.route('/members/<member_id>', methods=['PUT'])
def modify_member(member_id):
    data = request.json
    updated_member = update_member(member_id, data)
    if updated_member:
        return jsonify(updated_member), 200
    return jsonify({'message': 'Member not found'}), 404


@member_blueprint.route('/members/<member_id>', methods=['DELETE'])
def remove_member(member_id):
    deleted_member = delete_member(member_id)
    if deleted_member:
        return jsonify({'message': 'Member deleted'}), 200
    return jsonify({'message': 'Member not found'}), 404

@member_blueprint.route('/members/signup', methods=['POST'])
def signup():
    data= request.get_json()
    if not data.get('member_id') or not data.get('password'):
        return jsonify({"message": "Member ID and password are required"}), 400
    
    new_member= signup_member(data)
    if not new_member:
        return jsonify({"message": "Member ID already exists"}), 400
    
    return jsonify(new_member.to_dict()), 201


@member_blueprint.route('/members/login', methods=['POST'])
def login():
    
    data = request.json
    member_id = data.get('member_id')
    password = data.get('password')

    if not member_id or not password:
        return jsonify({"message": "Member ID and password are required"}), 400

    member = login_member(member_id, password)
    if not member:
        return jsonify({"message": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful", "member": member.to_dict()}), 200
