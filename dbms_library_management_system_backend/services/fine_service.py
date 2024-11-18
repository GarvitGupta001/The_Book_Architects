from utils.utils import db
from models.fine_model import FineModel
from models.transaction_model import TransactionModel

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

def get_fine_by_id(fine_id):
    fine= FineModel.query.get(fine_id)
    return fine.to_dict()


def update_fine(fine_id, amount=None, days_delay=None, member_id=None):
    fine = FineModel.query.get(fine_id)
    if fine:
        if amount:
            fine.amount = amount
        if days_delay:
            fine.days_delay = days_delay
        if member_id:
            fine.member_id = member_id
        
        db.session.commit()
        return fine.to_dict()
    
    return fine


def delete_fine(fine_id):
    fine = get_fine_by_id(fine_id)
    if fine:
        db.session.delete(fine)
        db.session.commit()
    return fine

def calculate_and_store_fine(transaction_id):
    
    transaction = TransactionModel.query.get(transaction_id)
    if not transaction:
        return {'error': 'Transaction not found'}

    fine_data = transaction.calculate_fine()
    if fine_data['overdue_days'] > 0:
        # Create a fine entry if there are overdue days
        fine = FineModel(
            fine_id=f"F{transaction_id}",  # Unique fine ID
            amount=fine_data['fine_amount'],
            days_delay=fine_data['overdue_days'],
            member_id=transaction.member_id
        )
        db.session.add(fine)
        db.session.commit()
        return {
            'message': 'Fine calculated and stored successfully',
            'fine_id': fine.fine_id,
            'amount': fine.amount,
            'days_delay': fine.days_delay
        }
    return {
        'message': 'No fine applicable',
        'fine_amount': 0,
        'overdue_days': 0
    }
