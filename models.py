
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import or_, desc, func
import data


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
# app.url_map.strict_slashes = False
db = SQLAlchemy(app)

# Создаем модели

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    start_date = db.Column(db.String(100))
    end_date = db.Column(db.String(100))
    address = db.Column(db.String(100))
    price = db.Column(db.Float)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    customer = relationship("User", foreign_keys=[customer_id])
    executor = relationship("User", foreign_keys=[executor_id])

class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    order = relationship("Order", foreign_keys=[order_id])
    executor = relationship("User", foreign_keys=[executor_id])

db.create_all()

# Добавляем данные в таблицы
for user in data.USERS:
    db.session.add(User(
       id=user['id'],
       first_name=user['first_name'],
       last_name=user['last_name'],
       age=user['age'],
       email=user['email'],
       role=user['role'],
       phone=user['phone'])
    )
    db.session.commit()

for order in data.ORDERS:
    db.session.add(Order(
        id=order['id'],
        name=order['name'],
        description=order['description'],
        start_date=order['start_date'],
        end_date=order['end_date'],
        address=order['address'],
        price=order['price'],
        customer_id=order['customer_id'],
        executor_id=order['executor_id'])
    )
    db.session.commit()

for offer in data.OFFERS:
    db.session.add(Offer(
        id=offer['id'],
        order_id=offer['order_id'],
        executor_id=offer['executor_id'])
    )
    db.session.commit()

db.session.close()
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run(Debug=True)

