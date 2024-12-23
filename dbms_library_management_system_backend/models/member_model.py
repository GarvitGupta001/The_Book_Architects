from utils.utils import db
from werkzeug.security import generate_password_hash, check_password_hash
class MemberModel(db.Model):
    __tablename__ = 'member'
    member_id = db.Column(db.String(10), primary_key=True)
    member_name = db.Column(db.String(50), nullable=False)
    member_type = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    date_of_joining = db.Column(db.Date, nullable=False)
    member_course = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    street = db.Column(db.Integer)
    password = db.Column(db.String(255), nullable=False)
    member_email = db.Column(db.String(50),unique= True, nullable=False)
    member_phone = db.Column(db.BigInteger, nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
  
    def __repr__(self):
        return f"<Member {self.member_name} - ID: {self.member_id}>"
    
    def to_dict(self):
        return {
            'member_id': self.member_id,
            'member_name': self.member_name,
            'member_type': self.member_type,
            'date_of_birth': self.date_of_birth.isoformat() if self.date_of_birth else None,
            'date_of_joining': self.date_of_joining.isoformat() if self.date_of_joining else None,
            'member_course': self.member_course,
            'country': self.country,
            'state': self.state,
            'city': self.city,
            'street': self.street,
            'member_email': self.member_email,
            'member_phone': self.member_phone,
            'gender': self.gender,
            
        }