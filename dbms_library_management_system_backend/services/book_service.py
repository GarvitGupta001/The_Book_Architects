from utils.utils import db
from models.book_model import BookModel

def create_book(data):
    new_book = BookModel(
        book_id=data.get('book_id'),
        author_id=data.get('author_id'),
        book_title=data.get('book_title'),
        publisher_id=data.get('publisher_id'),
        vendor_id=data.get('vendor_id'),
        shelf_id=data.get('shelf_id'),
        category=data.get('category'),
        price=data.get('price'),
        language_name=data.get('language_name'),
        subject_name=data.get('subject_name'),
        genre=data.get('genre'),
        date_of_publishing=data.get('date_of_publishing'),
        date_of_addition=data.get('date_of_addition'),
        availability=data.get('availability'),
        shelf_date=data.get('shelf_date'),
        bought_on=data.get('bought_on')
    )
    db.session.add(new_book)
    db.session.commit()
    return new_book


def get_book_by_id(book_id):
    book= BookModel.query.get(book_id)
    return book.to_dict()

def update_book(book_id, author_id=None, book_title=None, publisher_id=None, vendor_id=None, shelf_id=None,
                category=None, price=None, language_name=None, subject_name=None, genre=None,
                date_of_publishing=None, date_of_addition=None, shelf_date=None, bought_on=None, availability=None):
    book = BookModel.query.get(book_id)
    if book:
        if author_id:
            book.author_id = author_id.get('author_id', book.author_id)
        if book_title:
            book.book_title = book_title.get('book_title', book.book_title)
        if publisher_id:
            book.publisher_id = publisher_id.get('publisher_id', book.publisher_id)
        if vendor_id:
            book.vendor_id = vendor_id.get('vendor_id', book.vendor_id)
        if shelf_id:
            book.shelf_id = shelf_id.get('shelf_id', book.shelf_id)
        if category:
            book.category = category.get('category', book.category)
        if price:
            book.price = price.get('price', book.price)
        if language_name:
            book.language_name = language_name.get('language_name', book.language_name)
        if subject_name:
            book.subject_name = subject_name.get('subject_name', book.subject_name)
        if genre:
            book.genre = genre.get('genre', book.genre)
        
        if date_of_publishing:
            book.date_of_publishing = date_of_publishing.get('date_of_publishing', book.date_of_publishing)
        if date_of_addition:
            book.date_of_addition = date_of_addition.get('date_of_addition', book.date_of_addition)
        if shelf_date:
            book.shelf_date = shelf_date.get('shelf_date', book.shelf_date)
        if bought_on:
            book.bought_on = bought_on.get('bought_on', book.bought_on)

        if availability is not None:
            book.availability = availability.get('availability', book.availability)
        
        db.session.commit()
        return book.to_dict()
    
    return book



def delete_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return True
    return False
