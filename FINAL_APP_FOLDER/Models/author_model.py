from utils.utils import db


class Authors(db.Model):
    __tablename__ = 'author'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    origin = db.Column(db.Text)
    about = db.Column(db.Text)

    def __repr__(self):
        return f"<Author {self.name}>"
    def to_dict(self):
        """Convert the AuthorModel instance into a dictionary format."""
        return {
            'id': self.id,
            'name': self.name,
            'dob': self.dob,
            'origin': self.origin,
            'about':self.about,
        }