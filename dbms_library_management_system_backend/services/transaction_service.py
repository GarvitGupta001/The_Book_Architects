from utils.utils import db
from models.transaction_model import TransactionModel
from datetime import datetime, timedelta
from models.book_model import BookModel
def add_transaction(data):
    transaction = TransactionModel(
        transaction_id=data.get('transaction_id'),
        return_date=data.get('return_date'),
        issue_date=data.get('transaction_date'),
        employee_id=data.get('employee_id'),
        member_id=data.get('member_id'),
        book_id=data.get('book_id')
    )
    db.session.add(transaction)
    db.session.commit()
    return transaction


def get_transaction_by_id(transaction_id):
    transaction= TransactionModel.query.get(transaction_id)
    return transaction.to_dict()


def update_transaction(transaction_id, return_date=None, issue_date=None, employee_id=None, member_id=None, book_id=None):
    transaction = TransactionModel.query.get(transaction_id)
    if transaction:
        if return_date:
            transaction.return_date =return_date
        if issue_date:
            transaction.issue_date =issue_date
        if employee_id:
            transaction.employee_id = employee_id
        if member_id:
            transaction.member_id = member_id
        if book_id:
            transaction.book_id = book_id
        
        db.session.commit()
        return transaction.to_dict()
    
    return transaction



def delete_transaction(transaction_id):
    transaction = get_transaction_by_id(transaction_id)
    if transaction:
        db.session.delete(transaction)
        db.session.commit()
    return transaction


def get_books_issued_by_member(member_id):
    
    transactions = db.session.query(TransactionModel).filter(
        TransactionModel.member_id == member_id
    ).all()

   
    if transactions:
        issued_books = []
        for transaction in transactions:
            issued_books.append(transaction.book.to_dict())  # Convert book to dictionary
        return issued_books
    return None 

def get_books_due_soon():
    today = datetime.now()
    next_week = today + timedelta(days=7)
    due_soon_books = db.session.query(TransactionModel).filter(
        TransactionModel.return_date >= today,
        TransactionModel.return_date <= next_week
    ).all()

    return [transaction.book.to_dict() for transaction in due_soon_books]
