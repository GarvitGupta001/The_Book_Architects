from utils.utils import db
from models.fine_model import FineModel

# Create a new fine
def create_fine(data):
    new_fine = FineModel(
        fine_id=data.get('fine_id'),
        amount=data.get('amount'),
        days_delay=data.get('days_delay'),
        member_id=data.get('member_id')
    )
    db.session.add(new_fine)
    db.session.commit()
    return new_fine

# Read (retrieve) a fine by ID
def get_fine_by_id(fine_id):
    fine= FineModel.query.get(fine_id)
    return fine.to_dict()

# Update a fine
def update_fine(fine_id, amount=None, days_delay=None, member_id=None):
    fine = FineModel.query.get(fine_id)
    if fine:
        if amount:
            fine.amount = amount.get('amount', fine.amount)
        if days_delay:
            fine.days_delay = days_delay.get('days_delay', fine.days_delay)
        if member_id:
            fine.member_id = member_id.get('member_id', fine.member_id)
        
        db.session.commit()
        return fine.to_dict()
    
    return fine


# Delete a fine by ID
def delete_fine(fine_id):
    fine = get_fine_by_id(fine_id)
    if fine:
        db.session.delete(fine)
        db.session.commit()
    return fine
