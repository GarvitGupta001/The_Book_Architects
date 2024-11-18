
from utils.utils import db
from models.author_model import AuthorModel
def create_author(author_id, author_name, author_dob, author_origin=None, about=None):
    new_author = AuthorModel(
        author_id=author_id,
        author_name=author_name,
        author_dob=author_dob,
        author_origin=author_origin,
        about=about
    )
    db.session.add(new_author)
    db.session.commit()
    return new_author

def get_author_by_id(author_id):
    author= AuthorModel.query.get(author_id)
    return author.to_dict()

def update_author(author_id, author_name=None, author_dob=None, author_origin=None, about=None):
    author = AuthorModel.query.get(author_id)
    if author:
        if author_name:
            author.author_name = author_name
        if author_dob:
            author.author_dob = author_dob
        if author_origin:
            author.author_origin = author_origin
        if about:
            author.about = about
        db.session.commit()
        return author.to_dict()
    return author

def delete_author(author_id):
    author = get_author_by_id(author_id)
    if author:
        db.session.delete(author)
        db.session.commit()
        return True
    return False