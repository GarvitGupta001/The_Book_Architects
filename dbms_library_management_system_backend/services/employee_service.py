from utils.utils import db
from models.employee_model import EmployeeModel

# Create a new employee
def create_employee(data):
    new_employee = EmployeeModel(
        employee_id=data.get('employee_id'),
        employee_name=data.get('employee_name'),
        employee_email=data.get('employee_email'),
        employee_phone=data.get('employee_phone'),
        gender=data.get('gender'),
        date_of_birth=data.get('date_of_birth'),
        date_of_joining=data.get('date_of_joining')
    )
    db.session.add(new_employee)
    db.session.commit()
    return new_employee

# Read (retrieve) an employee by ID
def get_employee_by_id(employee_id):
    employee= EmployeeModel.query.get(employee_id)
    return employee.to_dict()
# Update an employee's information
def update_employee(employee_id, employee_name=None, employee_email=None, employee_phone=None, gender=None, date_of_birth=None, date_of_joining=None):
    employee = EmployeeModel.query.get(employee_id)
    if employee:
        # Update only the provided fields
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

        db.session.commit() 
        return employee.to_dict() 
    
    return employee  

# Delete an employee by ID
def delete_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return True
    return False
