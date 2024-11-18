from utils.utils import db
from datetime import datetime, timedelta
from models.employee_model import EmployeeModel
from models.book_model import BookModel
from models.member_model import MemberModel

from pytz import timezone

IST= timezone('Asia/Kolkata')
class TransactionModel(db.Model):
    __tablename__ = 'transaction'
    transaction_id = db.Column(db.String(10), primary_key=True)
    return_date = db.Column(db.DateTime)  
    issue_date = db.Column(db.DateTime, default=datetime.now(IST), nullable=False)
    employee_id = db.Column(db.String(10), db.ForeignKey('employee.employee_id', onupdate="CASCADE"), nullable=False)
    member_id = db.Column(db.String(10), db.ForeignKey('member.member_id', onupdate="CASCADE"), nullable=False)
    book_id = db.Column(db.String(10), db.ForeignKey('book.book_id', onupdate="CASCADE"), nullable=False)

    # Relationships to retrieve related data if needed
    employee = db.relationship('EmployeeModel', backref='transactions', lazy=True)
    member = db.relationship('MemberModel', backref='transactions', lazy=True)
    book = db.relationship('BookModel', backref='transactions', lazy=True)

    def __repr__(self):
        return f"<Transaction {self.transaction_id} - {self.transaction_type}>"
    
    def to_dict(self):
        return {
            'transaction_id': self.transaction_id,
            'return_date': self.return_date,
            'issue_date': self.issue_date.isoformat() if self.issue_date else None,
            'employee_id': self.employee_id,
            'member_id': self.member_id,
            'book_id': self.book_id,
            'employee': self.employee.to_dict() if self.employee else None,
            'member': self.member.to_dict() if self.member else None,
            'book': self.book.to_dict() if self.book else None
        }
    
    def calculate_fine(self):
        """
        Calculates fine for the transaction if it is overdue.
        """
        if not self.return_date or not self.issue_date:
            return None 

        due_date = self.issue_date + timedelta(days=30)  # 30-day borrowing period
        if self.return_date > due_date:
            overdue_days = (self.return_date - due_date).days
            fine_amount = overdue_days * 5  # Fine: 5 rupees per overdue day
            return {
                'overdue_days': overdue_days,
                'fine_amount': fine_amount
            }
        return {
            'overdue_days': 0,
            'fine_amount': 0
        }