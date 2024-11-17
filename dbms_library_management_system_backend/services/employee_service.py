from utils.utils import db
from models.employee_model import EmployeeModel

def create_employee(data):
    new_employee = EmployeeModel(
        employee_id=data.get('employee_id'),
        employee_name=data.get('employee_name'),
        employee_email=data.get('employee_email'),
        employee_phone=data.get('employee_phone'),
        gender=data.get('gender'),
        date_of_birth=data.get('date_of_birth'),
        date_of_joining=data.get('date_of_joining'),
        password=data.get('password')
    )
    db.session.add(new_employee)
    db.session.commit()
    return new_employee

def get_employee_by_id(employee_id):
    employee= EmployeeModel.query.get(employee_id)
    return employee.to_dict()

def update_employee(employee_id, employee_name=None, employee_email=None, employee_phone=None, gender=None, date_of_birth=None, date_of_joining=None, password=None):
    employee = EmployeeModel.query.get(employee_id)
    if employee:
      
        if employee_name:
            employee.employee_name = employee_name.get('employee_name', employee.employee_name)
        if employee_email:
            employee.employee_email = employee_email.get('employee_email', employee.employee_email)
        if employee_phone:
            employee.employee_phone = employee_phone.get('employee_phone', employee.employee_phone)
        if gender:
            employee.gender = gender.get('gender', employee.gender)
        if date_of_birth:
            employee.date_of_birth = date_of_birth.get('date_of_birth', employee.date_of_birth)
        if date_of_joining:
            employee.date_of_joining = date_of_joining.get('date_of_joining', employee.date_of_joining)
        if password:
            employee.password= password.get('password', employee.password)

        db.session.commit() 
        return employee.to_dict() 
    
    return employee  


def delete_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return True
    return False

def signup_employee(data):
    
    if EmployeeModel.query.get(data['employee_id']):
        return None

    new_employee = EmployeeModel(
        employee_id=data['employee_id'],
        employee_name=data['employee_name'],
        employee_email=data['employee_email'],
        employee_phone=data['employee_phone'],
        gender=data['gender'],
        date_of_birth=data['date_of_birth'],
        date_of_joining=data['date_of_joining']
    )
    new_employee.set_password(data['password'])
    db.session.add(new_employee)
    db.session.commit()
    
    return new_employee


def login_employee(employee_id, password):
    employee = EmployeeModel.query.get(employee_id)
    if employee and employee.check_password(password): 
        return employee
    return None