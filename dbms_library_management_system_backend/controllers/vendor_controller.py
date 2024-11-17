from flask import Blueprint, jsonify, request
from services.vendor_service import add_vendor, get_vendor_by_id, update_vendor, delete_vendor
from models.vendor_model import VendorModel
vendor_blueprint = Blueprint('vendors', __name__)

@vendor_blueprint.route('/vendors', methods=['POST'])
def create_vendor():
    data = request.json
    new_vendor = add_vendor(data)
    return jsonify(new_vendor.to_dict()), 201


@vendor_blueprint.route('/vendors/<vendor_id>', methods=['GET'])
def retrieve_vendor(vendor_id):
    vendor = get_vendor_by_id(vendor_id)
    if vendor:
        return jsonify(vendor), 200
    return jsonify({'message': 'Vendor not found'}), 404

@vendor_blueprint.route('/vendors/<vendor_id>', methods=['PUT'])
def modify_vendor(vendor_id):
    data = request.json
    updated_vendor = update_vendor(vendor_id, data)
    if updated_vendor:
        return jsonify(updated_vendor), 200
    return jsonify({'message': 'Vendor not found'}), 404

@vendor_blueprint.route('/vendors/<vendor_id>', methods=['DELETE'])
def remove_vendor(vendor_id):
    deleted_vendor = delete_vendor(vendor_id)
    if deleted_vendor:
        return jsonify({'message': 'Vendor deleted'}), 200
    return jsonify({'message': 'Vendor not found'}), 404
