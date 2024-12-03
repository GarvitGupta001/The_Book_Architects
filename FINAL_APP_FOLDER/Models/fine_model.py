from utils.utils import db
from datetime import datetime
from Models.employee_model import Employees
from Models.book_model import Books
from Models.member_model import Members
from Models.transaction_model import Transactions

class Fines(db.Model):
    __tablename__ = 'fine'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    days_delay = db.Column(db.Integer, nullable=False)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transaction.id', onupdate="CASCADE"), nullable=False)

    transaction = db.relationship("Transactions", backref=db.backref("fine", lazy=True))

    def __repr__(self):
        return f"<Fine {self.id} - Amount: {self.amount}>"
    def to_dict(self):
        """Convert the FineModel instance into a dictionary format."""
        return {
            'id': self.id,
            'amount': self.amount,
            'days_delay': self.days_delay,
            'transaction': self.transaction.to_dict() if self.transaction else None
        }