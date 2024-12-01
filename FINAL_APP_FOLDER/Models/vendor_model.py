from utils.utils import db
from flask import Flask
class Vendors(db.Model):
    __tablename__ = 'vendor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.Text, nullable=False)
    about = db.Column(db.Text)

    def __repr__(self):
        return f"<Vendor {self.name}>"
    
    def to_dict(self):
        """Convert the VendorModel instance into a dictionary format."""
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'about': self.about,
        }
    
    