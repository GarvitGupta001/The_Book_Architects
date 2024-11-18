from utils.utils import db
from models.vendor_model import VendorModel

def add_vendor(data):
    vendor = VendorModel(
        vendor_id=data.get('vendor_id'),
        vendor_name=data.get('vendor_name'),
        vendor_address=data.get('vendor_address'),
        about=data.get('about')
    )
    db.session.add(vendor)
    db.session.commit()
    return vendor

def get_vendor_by_id(vendor_id):
    vendor= VendorModel.query.get(vendor_id)
    return vendor.to_dict() if vendor else None


def update_vendor(vendor_id, vendor_name=None, vendor_address=None, about=None):
    vendor = VendorModel.query.get(vendor_id)
    if vendor:
        if vendor_name:
            vendor.vendor_name = vendor_name.get('vendor_name', vendor.vendor_name)
        if vendor_address:
            vendor.vendor_address = vendor_address.get('vendor_address', vendor.vendor_address)
        if about:
            vendor.about = about.get('about', vendor.about)
        
        db.session.commit()
        return vendor.to_dict()
    return vendor


def delete_vendor(vendor_id):
    vendor = VendorModel.query.get(vendor_id)
    if vendor:
        db.session.delete(vendor)
        db.session.commit()
        return True
    return False
