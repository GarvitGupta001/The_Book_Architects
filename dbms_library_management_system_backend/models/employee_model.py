from utils.utils import db
from werkzeug.security import generate_password_hash, check_password_hash
class EmployeeModel(db.Model):
    __tablename__ = 'employee'
    employee_id = db.Column(db.String(10), primary_key=True)
    employee_name = db.Column(db.String(50), nullable=False)
    employee_email = db.Column(db.String(50), nullable=False)
    employee_phone = db.Column(db.BigInteger, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    date_of_joining = db.Column(db.Date, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    street = db.Column(db.Integer)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


    def __repr__(self):
        return f"<Employee {self.employee_name}>"
    
    def to_dict(self):
       
        return {
            'employee_id': self.employee_id,
            'employee_name': self.employee_name,
            'employee_email': self.employee_email,
            'employee_phone': self.employee_phone,
            'gender': self.gender,
            'date_of_birth': self.date_of_birth.isoformat() if self.date_of_birth else None,
            'date_of_joining': self.date_of_joining.isoformat() if self.date_of_joining else None,
            'country': self.country,
            'state': self.state,
            'city': self.city,
            'street': self.street,
            
        }