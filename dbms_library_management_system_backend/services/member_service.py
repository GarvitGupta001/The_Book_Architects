from utils.utils import db
from models.member_model import MemberModel
from flask import session

def create_member(data):
    new_member = MemberModel(
        member_id=data.get('member_id'),
        member_name=data.get('member_name'),
        member_type=data.get('member_type'),
        date_of_birth=data.get('date_of_birth'),
        date_of_joining=data.get('date_of_joining'),
        member_course=data.get('member_course'),
        country=data.get('country'),
        state=data.get('state'),
        city=data.get('city'),
        street=data.get('street'),
        password=data.get('password'),
        member_email=data.get['employee_email'],
        member_phone=data.get['employee_phone'],
        gender=data.get['gender'],
    )
    db.session.add(new_member)
    db.session.commit()
    return new_member


def get_member_by_id(member_id):
    member= MemberModel.query.get(member_id)
    return member.to_dict()

def update_member(member_id, member_name=None, member_type=None, date_of_birth=None, date_of_joining=None,
                  member_course=None, country=None, state=None, city=None, street=None, password= None, member_email=None, member_phone=None, gender=None):
    member = MemberModel.query.get(member_id )
    if member:
       
        if member_name:
            member.member_name = member_name
        if member_type:
            member.member_type = member_type
        if date_of_birth:
            member.date_of_birth = date_of_birth
        if date_of_joining:
            member.date_of_joining = date_of_joining
        if member_course:
            member.member_course = member_course
        if country:
            member.country = country
        if state:
            member.state = state
        if city:
            member.city = city
        if street:
            member.street = street
        if password:
            member.password= password
        if member_email:
            member.member_email= member_email
        if member_phone:
            member.member_phone= member_phone
        if gender:
            member.gender= gender
        

        db.session.commit()
        return member.to_dict() 
    return member


def delete_member(member_id):
    member = get_member_by_id(member_id)
    if member:
        db.session.delete(member)
        db.session.commit()
    return member

def signup_member(data):
    
    if MemberModel.query.filter_by(member_email=data['member_email']).first():
        return None

    
    new_member = MemberModel(
        member_id=data['member_id'],
        member_name=data['member_name'],
        member_type=data['member_type'],
        date_of_birth=data['date_of_birth'],
        date_of_joining=data['date_of_joining'],
        member_course=data['member_course'],
        country=data['country'],
        state=data['state'],
        city=data['city'],
        street=data['street'],
        member_email=data['member_email'],
        member_phone=data['member_phone'],
        gender=data['gender'],
    )
    
    new_member.set_password(data['password'])
    
   
    db.session.add(new_member)
    db.session.commit()
    
    return new_member

def login_member(member_email, password):
    member= MemberModel.query.filter_by(member_email= member_email).first()
    if member and member.check_password(password):
        session['logged_in']= True
        session['member_email']= member.member_email      
        return member
    return None

def logout_member():
    if 'logged_in' in session:
        session.clear()
        return {"message": "Logout successful"}
    return {"error": "No active session"}