from utils.utils import db
from models.member_model import MemberModel


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
        password=data.get('password')
    )
    db.session.add(new_member)
    db.session.commit()
    return new_member


def get_member_by_id(member_id):
    member= MemberModel.query.get(member_id)
    return member.to_dict()

def update_member(member_id, member_name=None, member_type=None, date_of_birth=None, date_of_joining=None,
                  member_course=None, country=None, state=None, city=None, street=None, password= None):
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
    
    if MemberModel.query.get(data['member_id']):
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
    )
    
    new_member.set_password(data['password'])
    
   
    db.session.add(new_member)
    db.session.commit()
    
    return new_member

def login_member(member_id, password):
    member= MemberModel.query.get(member_id)
    if member and member.check_password(password):
        return member
    return None