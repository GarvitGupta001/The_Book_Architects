from utils.utils import db
from models.shelf_model import ShelfModel

# Create a new shelf
def create_shelf(data):
    new_shelf = ShelfModel(
        shelf_id=data.get('shelf_id'),
        quantity=data.get('quantity'),
        shelf_floor=data.get('shelf_floor'),
        shelf_rows=data.get('shelf_rows'),
        shelf_cols=data.get('shelf_cols')
    )
    db.session.add(new_shelf)
    db.session.commit()
    return new_shelf

# Retrieve a shelf by ID
def get_shelf_by_id(shelf_id):
    shelf=ShelfModel.query.get(shelf_id)
    return shelf.to_dict()

# Update shelf information
def update_shelf(shelf_id, quantity=None, shelf_floor=None, shelf_rows=None, shelf_cols=None):
    shelf = get_shelf_by_id(shelf_id)
    if shelf:
        if quantity: 
            shelf.quantity = quantity.get('quantity', shelf.quantity)
        if shelf_floor:
            shelf.shelf_floor = shelf_floor.get('shelf_floor', shelf.shelf_floor)
        if shelf_rows:
            shelf.shelf_rows = shelf_rows.get('shelf_rows', shelf.shelf_rows)
        if shelf_cols:
            shelf.shelf_cols = shelf_cols.get('shelf_cols', shelf.shelf_cols)
        db.session.commit()
        return shelf.to_dict()
    return shelf

# Delete a shelf by ID
def delete_shelf(shelf_id):
    shelf = get_shelf_by_id(shelf_id)
    if shelf:
        db.session.delete(shelf)
        db.session.commit()
        return True
    return False
