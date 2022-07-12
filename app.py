from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
# app.url_map.strict_slashes = False
db = SQLAlchemy(app)

def instance_to_dict(instance):
    return {
        "id": instance.id,
        "first_name": instance.first_name,
        "last_name": instance.last_name,
        "age": instance.age,
        "email": instance.email,
        "role": instance.role,
        "phone": instance.phone
    }

@app.route('/users/')
def get_all_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append(instance_to_dict(user))
    print(result)
    return jsonify(result)


if __name__ == '__main__':
    app.run(Debug=True)