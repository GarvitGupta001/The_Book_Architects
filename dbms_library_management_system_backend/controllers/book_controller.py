from flask import Blueprint, jsonify, request
from services.book_service import create_book, get_book_by_id, update_book, delete_book, search_books, get_books_by_genre, get_books_by_author_and_publisher
from models.book_model import BookModel
book_blueprint = Blueprint('books', __name__)


@book_blueprint.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = create_book(data)
    return jsonify(new_book.to_dict()), 201


@book_blueprint.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({'message': 'Book not found'}), 404


@book_blueprint.route('/books/<book_id>', methods=['PUT'])
def modify_book(book_id):
    data = request.json
    updated_book = update_book(book_id, data)
    if updated_book:
        return jsonify(updated_book), 200
    return jsonify({'message': 'Book not found'}), 404


@book_blueprint.route('/books/<book_id>', methods=['DELETE'])
def remove_book(book_id):
    deleted_book = delete_book(book_id)
    if deleted_book:
        return jsonify({'message': 'Book deleted'}), 200
    return jsonify({'message': 'Book not found'}), 404

@book_blueprint.route('/books/search/<book_name>', methods=['GET'])
def search_book():
    book_name = request.args.get('book_name')
    
    if not book_name:
        return jsonify({"message": "No book name provided"}), 400
    
    result = search_books(book_name)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"message": "No books found matching the search term"}), 404

@book_blueprint.route('/books/genre/<genre>', methods=['GET'])
def list_books_by_genre(genre):
    books = get_books_by_genre(genre)
    if books:
        return jsonify(books), 200
    return jsonify({'message': 'No books found for this genre.'}), 404


@book_blueprint.route('/books/search', methods=['GET'])
def search_books_by_author_and_publisher():
    author_id = request.args.get('author_id')
    publisher_id = request.args.get('publisher_id')
    books = get_books_by_author_and_publisher(author_id, publisher_id)
    if books:
        return jsonify(books), 200
    return jsonify({'message': 'No books found for this author and publisher.'}), 404
