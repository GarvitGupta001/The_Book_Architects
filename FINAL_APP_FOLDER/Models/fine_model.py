from utils.utils import db
from datetime import datetime
from Models.employee_model import Employees
from Models.book_model import Books
from Models.member_model import Members
from Models.transaction_model import Transactions

class Fines(db.Model):
    __tablename__ = 'fine'
    id = db.Column(db.Integer, primary_key=True)
    issue_id = db.Column(db.Integer, db.ForeignKey('transaction.id', onupdate="CASCADE"), nullable=False)
    return_id = db.Column(db.Integer, db.ForeignKey('transaction.id', onupdate="CASCADE"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    days_delay = db.Column(db.Date, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id', onupdate="CASCADE"), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id', onupdate="CASCADE"), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id', onupdate="CASCADE"), nullable=False)

    member = db.relationship("MemberModel", backref=db.backref("fines", lazy=True))

    def __repr__(self):
        return f"<Fine {self.id} - Amount: {self.amount}>"
    def to_dict(self):
        """Convert the FineModel instance into a dictionary format."""
        return {
            'fine_id': self.id,

            'amount': self.amount,
            'issue_id': self.issue_id,
            'return_id': self.return_id,
            'issue': self.transaction.to_dict() if self.transaction else None,
            'return': self.transaction.to_dict() if self.transaction else None,
            'days_delay': self.days_delay,
            'date': self.date if self.date else None,
            'employee_id': self.employee_id,
            'member_id': self.member_id,
            'book_id': self.book_id,
            'book_title':Books.query.filter_by(id = self.book_id).first().title,
            'employee': self.employee.to_dict() if self.employee else None,
            'member': self.member.to_dict() if self.member else None,
            'book': self.book.to_dict() if self.book else None
        }