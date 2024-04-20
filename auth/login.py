from flask import request, jsonify
from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta
from models.user import User
from main import app



def login():
    auth = request.get_json()
    if not auth or not auth["username"] or not auth["password"]:
        return jsonify({"message": "Please provide username and password!"})

    user = User.query.filter_by(username=auth["username"]).first()

    if not user:
        return jsonify({"message": "User not found!"})

    if check_password_hash(user.password, auth["password"]):
        token = jwt.encode(
            {
                "public_id": user.public_id,
                "exp": datetime.utcnow() + timedelta(days=7),
            },
            app.config["SECRET_KEY"],
        )

        user_data = {
            "public_id": user.public_id,
            "username": user.username,
            "email": user.email,
        }
        return jsonify({"token": token, "user": user_data})

    return jsonify({"message": "Invalid credentials!"})
