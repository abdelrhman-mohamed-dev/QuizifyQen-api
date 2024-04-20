from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid
import jwt
#from jwt import encode
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import json
import os

app = Flask(__name__)


from auth.register import register_user
from auth import login

from models.user import User
from models.quiz import Quiz

from db_config import db

from routes.admin import get_all_users
from routes.admin import delete_all_users
from routes.admin import make_user_admin
from routes.admin import delete_all_quizzes

from routes.user import get_user_data
from routes.user import edit_user_data
from routes.user import delete_user_data

from routes.quiz import create_quiz
from routes.quiz import share_quiz
from routes.quiz import get_all_quizzes_of_user
from routes.quiz import get_one_quiz_with_id
from routes.quiz import delete_one_quiz_with_id
from routes.quiz import get_all_shared_quizzes




#QuizifyHub-api

app.config["SECRET_KEY"] = "mysecretkey"
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://questgen_user:girz2SJq0pu2QQk2SDy2AL9FJTSorEai@dpg-cns54kdjm4es73a7hm4g-a.oregon-postgres.render.com/questgen"
# postgresql://questgen_user:girz2SJq0pu2QQk2SDy2AL9FJTSorEai@dpg-cns54kdjm4es73a7hm4g-a.oregon-postgres.render.com/questgen
# app.config["UpLOAD_FOLDER"] = "/home/user/questgen/src/uploads"
app.config["ALLOWED_EXTENSIONS"] = {"pdf"}


# Initialize SQLAlchemy
db.init_app(app)


def create_database_tables():
    with app.app_context():
        db.create_all()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]

        if not token:
            return jsonify({"message": "Token is missing!"})

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.query.filter_by(public_id=data["public_id"]).first()
        except jwt.ExpiredSignatureError as e:
            return jsonify({"message": "Token has expired!"})
        except jwt.InvalidTokenError as e:
            return jsonify({"message": "Token is invalid!"})

        return f(current_user, *args, **kwargs)

    return decorated


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


@app.route("/", methods=["GET"])
def index():
    return "api working!"


# ======= admin routes ========

# get all users
@app.route("/api/v1/admin/user", methods=["GET"])
@token_required
def admin_get_all_users(current_user):
    return get_all_users(current_user)

# delete all users
@app.route("/api/v1/admin/user", methods=["DELETE"])
@token_required
def admin_delete_all_users(current_user):
    return delete_all_users(current_user)

# make user admin
@app.route("/api/v1/admin/user/<public_id>", methods=["PUT"])
@token_required
def admin_make_user_admin(current_user, public_id):
    return make_user_admin(current_user, public_id)

# delete all quizzes
@app.route("/api/v1/admin/quiz", methods=["DELETE"])
@token_required
def admin_delete_all_quizzes(current_user):
    return delete_all_quizzes(current_user)

# ======= end of admin routes ========


# ======= user routes =======

# get user data
@app.route("/api/v1/user/<public_id>", methods=["GET"])
@token_required
def get_one_user(current_user, public_id):
    return get_user_data(current_user, public_id)


# edit user data
@app.route("/api/v1/user/<public_id>", methods=["PUT"])
@token_required
def update_user(current_user, public_id):
    return edit_user_data(current_user, public_id)

#delete user data
@app.route("/api/v1/user/<public_id>", methods=["DELETE"])
@token_required
def delete_user(current_user, public_id):
    return delete_user_data(current_user, public_id)

# ======= end of user routes =======s


# ======= quiz routes =======

# create quiz
@app.route("/api/v1/create-quiz", methods=["POST"])
@token_required
def make_new_quiz(current_user):
    return create_quiz(current_user)

# share quiz
@app.route("/api/v1/share-quiz/<quiz_id>", methods=["PUT"])
@token_required
def revial_quiz(current_user,quiz_id):
    return share_quiz(current_user,quiz_id)

# get all quizs of user
@app.route("/api/v1/user/quiz", methods=["GET"])
@token_required
def get_all_quizzes(current_user):
    return get_all_quizzes_of_user(current_user)

# get one quiz
@app.route("/api/v1/user/quiz/<quiz_id>", methods=["GET"])
@token_required
def get_one_quiz(current_user,quiz_id):
    return get_one_quiz_with_id(current_user,quiz_id)

#delete quiz
@app.route("/api/v1/user/quiz/<quiz_id>", methods=["DELETE"])
@token_required
def delete_one_quiz(current_user,quiz_id):
    return delete_one_quiz_with_id(current_user,quiz_id)

# get all shared quizs
@app.route("/api/v1/shared-quiz", methods=["GET"])
@token_required
def shared_quizzes(current_user):
    return get_all_shared_quizzes(current_user)

# edit quiz with id
# @app.route("/api/v1/user/quiz/<quiz_id>", methods=["PUT"])
# @token_required
# def edit_one_quiz(current_user,quiz_id):
#     quiz = Quiz.query.filter_by(id=quiz_id).first()
#     if not quiz:
#         return jsonify({"message": "Quiz not found"})
#     if quiz.user_id != current_user.public_id:
#         return jsonify({"message": "You are not authorized to edit this quiz"})
    
# ======= end of quiz routes =======

# ======= auth routes =======
@app.route("/api/v1/login", methods=["POST"])
def login_route():
    return  login.login()  # Call the login function from login.py



@app.route("/api/v1/register", methods=["POST"])
def register_route():
    return register_user()

# ======= end of auth routes =======



if __name__ == "__main__":
    create_database_tables()
    app.run(debug=True, port=8080)
