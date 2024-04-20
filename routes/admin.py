from models.user import User
from flask import jsonify
from db_config import db
from models.quiz import Quiz

def get_all_users(current_user):
    # Check if the current user is an admin
    # if not current_user.admin:
    #     return jsonify({"message": "Cannot perform that function!"}), 403  # Return a response indicating the user is not authorized, with status code 403

    # Query all users from the database
    users = User.query.all()

    # Prepare the output data
    output = []
    for user in users:
        user_data = {
            "id": user.id,
            "public_id": user.public_id,
            "username": user.username,
            "email": user.email,
            "admin": user.admin,
            "activated": user.activated,
            "password": user.password,  # Note: It's generally not recommended to include passwords in the response
        }
        output.append(user_data)

    # Return a JSON response with the list of users
    return jsonify({"users": output}), 200  # Return a successful response with status code 200


def delete_all_users(current_user):

    if not current_user.admin:
        return jsonify({"message": "Cannot perform that function!"})

    users = User.query.all()
    for user in users:
        db.session.delete(user)
        db.session.commit()
    return jsonify({"message": "All users deleted successfully!"})


def make_user_admin(current_user, public_id):

    if not current_user.admin:
        return jsonify({"message": "Cannot perform that function!"})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({"message": "No user found!"})
    user.admin = True
    db.session.commit()
    return jsonify({"message": "User updated successfully!"})

def delete_all_quizzes(current_user):

    if not current_user.admin:
        return jsonify({"message": "Cannot perform that function!"})

    quizes = Quiz.query.all()
    for quiz in quizes:
        db.session.delete(quiz)
        db.session.commit()
    return jsonify({"message": "All quizes deleted successfully!"})