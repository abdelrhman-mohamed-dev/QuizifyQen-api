from flask import request, jsonify
from werkzeug.security import generate_password_hash
import uuid
from db_config import db
from models.user import User


def register_user():
    data = request.get_json()
    if not data or not data["username"] or not data["password"]:
        return jsonify({"message": "Please provide username and password!"})

    # Check if the username already exists
    existing_user = User.query.filter_by(username=data["username"]).first()
    if existing_user:
        return jsonify({"message": "Username already in use. Please choose a different one!"})

    hashed_password = generate_password_hash(data["password"], method="pbkdf2:sha256")
    new_user = User(
        public_id=str(uuid.uuid4()),
        username=data["username"],
        email=data.get("email"),  # Use data.get("email") to handle the case when "email" is not provided
        password=hashed_password,
        admin=False,
        activated=True,
    )
    db.session.add(new_user)
    db.session.commit()

    user_data = {
        "public_id": new_user.public_id,
        "username": new_user.username,
        "email": new_user.email,
    }
    return jsonify({"message": "User created successfully", "user": user_data})