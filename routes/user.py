from models.user import User
from flask import jsonify , request
from db_config import db
from werkzeug.security import generate_password_hash, check_password_hash


def get_user_data(current_user, public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({"message": "No user found!"})
    user_data = {
        "public_id": user.public_id,
        "username": user.username,
        "email": user.email,
        "admin": user.admin,
        "activated": user.activated,
    }
    return jsonify({"user": user_data})


def edit_user_data(current_user, public_id):   
    if (public_id != current_user.public_id):
        return jsonify({"message": "Cannot perform that function!"})
    
    if not request.json["curent_password"]:
        return jsonify({"message": "Please provide current password!"})

    if not request.json["new_password"]:
        return jsonify({"message": "Please provide new password!"})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({"message": "No user found!"})


    if check_password_hash(user.password, request.json["curent_password"]):
        user.password = generate_password_hash(request.json["new_password"], method="pbkdf2:sha256")
    else:
        return jsonify({"message": "Wrong password!"})


    user.username = request.json["username"]
    db.session.commit()

    user_data = {
        "id": user.id,
        "public_id": user.public_id,
        "username": user.username,
        "email": user.email,
        "admin": user.admin,
        "activated": user.activated,
    }
    return jsonify({"message": "User updated successfully", "user": user_data})

def delete_user_data(current_user, public_id):

    if not current_user.admin:
        return jsonify({"message": "Cannot perform that function!"})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({"message": "No user found!"})
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully!"})
