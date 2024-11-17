from flask import Flask
from config.config import Config_
from flask_mysqldb import MySQL
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from utils.utils import db
from utils.utils import migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config_.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config_.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)
migrate.init_app(app, db)

from models.author_model import AuthorModel
from controllers.author_controller import author_blueprint
app.register_blueprint(author_blueprint)

from models.book_model import BookModel
from controllers.book_controller import book_blueprint
app.register_blueprint(book_blueprint)

from models.employee_model import EmployeeModel
from controllers.employee_controller import employee_blueprint
app.register_blueprint(employee_blueprint)

from models.fine_model import FineModel
from controllers.fine_controller import fine_blueprint
app.register_blueprint(fine_blueprint)

from models.member_model import MemberModel
from controllers.member_controller import member_blueprint
app.register_blueprint(member_blueprint)

from models.publisher_model import PublisherModel
from controllers.publisher_controller import publisher_blueprint
app.register_blueprint(publisher_blueprint)


from models.shelf_model import ShelfModel
from controllers.shelf_controller import shelf_blueprint
app.register_blueprint(shelf_blueprint)

from models.transaction_model import TransactionModel
from controllers.transaction_controller import transaction_blueprint
app.register_blueprint(transaction_blueprint)

from models.vendor_model import VendorModel
from controllers.vendor_controller import vendor_blueprint
app.register_blueprint(vendor_blueprint)

if __name__ == '__main__':
    app.run(debug=True)