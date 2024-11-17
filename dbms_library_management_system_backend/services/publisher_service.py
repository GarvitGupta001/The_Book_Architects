from utils.utils import db
from models.publisher_model import PublisherModel


def create_publisher(data):
    new_publisher = PublisherModel(
        publisher_id=data.get('publisher_id'),
        publisher_name=data.get('publisher_name'),
        publisher_address=data.get('publisher_address'),
        about=data.get('about')
    )
    db.session.add(new_publisher)
    db.session.commit()
    return new_publisher


def get_publisher_by_id(publisher_id):
    publisher= PublisherModel.query.get(publisher_id)
    return publisher.to_dict()


def update_publisher(publisher_id, publisher_name=None, publisher_address=None, about=None):
    publisher = get_publisher_by_id(publisher_id)
    if publisher:
        if publisher_name:
            publisher.publisher_name=publisher_name.get('publisher_name', publisher.publisher_name)
        if publisher_address:
            publisher.publisher_address=publisher_address.get('publisher_address',publisher.publisher_address)
        if about:
            publisher.about=about.get('about',publisher.about)
        db.session.commit()
        return publisher.to_dict()
    return publisher


def delete_publisher(publisher_id):
    publisher = get_publisher_by_id(publisher_id)
    if publisher:
        db.session.delete(publisher)
        db.session.commit()
        return True
    return False
