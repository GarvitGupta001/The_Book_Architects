from utils.utils import db
from models.member_model import MemberModel

# Create a new member
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
        street=data.get('street')
    )
    db.session.add(new_member)
    db.session.commit()
    return new_member

# Retrieve a member by ID
def get_member_by_id(member_id):
    member= MemberModel.query.get(member_id)
    return member.to_dict()

# Update member information
# Update member information
def update_member(member_id, member_name=None, member_type=None, date_of_birth=None, date_of_joining=None,
                  member_course=None, country=None, state=None, city=None, street=None):
    member = MemberModel.query.get(member_id)
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

        db.session.commit()
        return member.to_dict() 
    return member


# Delete a member by ID
def delete_member(member_id):
    member = get_member_by_id(member_id)
    if member:
        db.session.delete(member)
        db.session.commit()
    return member
