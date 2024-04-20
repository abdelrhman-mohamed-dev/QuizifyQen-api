import json
from flask import request, jsonify

from models.quiz import Quiz
from db_config import db


# create quiz
def create_quiz(current_user):

    # Check if the PDF file is present in the request files
    if "pdf_file" not in request.files:
        return jsonify({"message": "No PDF file part!"})

    # Access the PDF file from the request
    pdf_file = request.files["pdf_file"]

    # Check if questions_number is present in the form data
    if "questions_number" not in request.form:
        return jsonify({"message": "No questions number provided!"})
    questions_number = request.form["questions_number"]

    # Check if questions_type is present in the form data
    if "questions_type" not in request.form:
        return jsonify({"message": "No questions type provided!"})
    
    questions_type = request.form["questions_type"]

    if questions_type not in ["mcq", "true_false"]:
        return jsonify({"message": "Invalid questions type!"})

    # Further processing logic can go here


    temp_content_json = {
        "questions": {
            "questions": [
                {
                    "answer": "computer system",
                    "context": "The main device categories are: The main parts of a computer system are: Input devices These devices are used to get data into the computer system Processing devices test test test These manipulate the data using to a set of instructions called a program Output devices These are used to get data out of a computer system Storage devices The can store the data for use at a later stage Communications devices These can send the data to another computer system 1 System Unit The container for the motherboard, disk drives etc. The main device categories are: The main parts of a computer system are: Input devices These devices are used to get data into the computer system Processing devices These manipulate the data using to a set of instructions called a program Output devices These are used to get data out of a computer system Storage devices The can store the data for use at a later stage Communications devices These can send the data to another computer system 1 System Unit The container for the motherboard, disk drives etc. The main device categories are: The main parts of a computer system are: Input devices These devices are used to get data into the computer system Processing devices These manipulate the data using to a set of instructions called a program Output devices These are used to get data out of a computer system Storage devices The can store the data for use at a later stage Communications devices These can send the data to another computer system 1 System Unit The container for the motherboard, disk drives etc.",
                    "extra_options": [
                        "Phone System",
                        "Physical Device",
                        "Security Protocols",
                    ],
                    "id": 1,
                    "options": ["Software Program", "Computer Network", "Mainframe"],
                    "options_algorithm": "sense2vec",
                    "question_statement": "What are the main parts of a computer system?",
                    "question_type": "MCQ",
                },
                {
                    "answer": "graphics cards",
                    "context": "The main parts of a graphics card are: Computers are often supplied with integrated graphics cards. This is called Scalable Link Interface (SLI) and it allows the two graphics cards to produce a single output. It also allows for the use of two graphics cards working in tandem to improve the performance.",
                    "extra_options": ["Processors"],
                    "id": 2,
                    "options": ["Video Cards", "Gpus", "Single Gpu"],
                    "options_algorithm": "sense2vec",
                    "question_statement": "What are the main parts of a graphics card?",
                    "question_type": "MCQ",
                },
                {
                    "answer": "software",
                    "context": "Examples include: • Motherboard • Hard disk • RAM • Power supply • Processor • Case • Monitor • Keyboard • Mouse Software: The term software is used to describe computer programs that perform a task or tasks on a computer system. Examples include: • Motherboard • Hard disk • RAM • Power supply • Processor • Case • Monitor • Keyboard • Mouse Software: The term software is used to describe computer programs that perform a task or tasks on a computer system. Software can be grouped as follows: • System software: These are the programs that control the operation of the computer system.",
                    "extra_options": [],
                    "id": 3,
                    "options": ["Hardware"],
                    "options_algorithm": "sense2vec",
                    "question_statement": "What is the term used to describe computer programs that perform a task on a computer system?",
                    "question_type": "MCQ",
                },
                {
                    "answer": "processor",
                    "context": "Below is shown typical power usage for a number of computer devices: • Motherboard: 60 watts • Processor: 90 watts • Memory: 10 watts/128MB • Processor fan: 5 watts • Graphics card: 40 watts • Hard disk: 25 watts • Optical drive: 30 watts As can be seen, a large power supply (at least 400 Watts) is preferable and does not use more energy as it only supplies power on demand. Below is shown typical power usage for a number of computer devices: • Motherboard: 60 watts • Processor: 90 watts • Memory: 10 watts/128MB • Processor fan: 5 watts • Graphics card: 40 watts • Hard disk: 25 watts • Optical drive: 30 watts As can be seen, a large power supply (at least 400 Watts) is preferable and does not use more energy as it only supplies power on demand. This is the speed of the system clock (clock speed) within the processor and it controls how fast instructions can be executed: • 1 MHz - One million clock ticks every second • 1 GHz - One billion clock ticks every second This means that if one instruction was executed every clock tick, a 3GHz processor could execute three billion instructions every second.",
                    "extra_options": ["Chipset", "Graphics Chip", "Video Card"],
                    "id": 4,
                    "options": ["Cpu.", "Ram", "Igpu"],
                    "options_algorithm": "sense2vec",
                    "question_statement": "What is the speed of the system clock within the processor?",
                    "question_type": "MCQ",
                },
                {
                    "answer": "disk",
                    "context": "The main device categories are: The main parts of a computer system are: Input devices These devices are used to get data into the computer system Processing devices These manipulate the data using to a set of instructions called a program Output devices These are used to get data out of a computer system Storage devices The can store the data for use at a later stage Communications devices These can send the data to another computer system 1 System Unit The container for the motherboard, disk drives etc. Below is shown typical power usage for a number of computer devices: • Motherboard: 60 watts • Processor: 90 watts • Memory: 10 watts/128MB • Processor fan: 5 watts • Graphics card: 40 watts • Hard disk: 25 watts • Optical drive: 30 watts As can be seen, a large power supply (at least 400 Watts) is preferable and does not use more energy as it only supplies power on demand. Examples include: • Motherboard • Hard disk • RAM • Power supply • Processor • Case • Monitor • Keyboard • Mouse Software: The term software is used to describe computer programs that perform a task or tasks on a computer system.",
                    "extra_options": [],
                    "id": 5,
                    "options": ["Hard Drive", "Boot Sector"],
                    "options_algorithm": "sense2vec",
                    "question_statement": "What is the main component of a computer system?",
                    "question_type": "MCQ",
                },
            ],
            "statement": "Hardware and Software A computer system is made up of a combination of hardware and software. Hardware: All of the electronic and mechanical equipment in a computer is called the hardware. Examples include: • Motherboard • Hard disk • RAM • Power supply • Processor • Case • Monitor • Keyboard • Mouse Software: The term software is used to describe computer programs that perform a task or tasks on a computer system. Software can be grouped as follows: • System software: These are the programs that control the operation of the computer system. Operating systems and utility programs are the most common. The Operating System starts the computer, provides a user interface, manages the computer memory, manages storage, manages security and provides networking",
            "time_taken": 167.42159605026245,
        }
    }

    # Convert content to string for database
    content = json.dumps(temp_content_json)

    # convert content to json
    json_content = json.loads(content)

    # Create a new Quiz object
    quiz = Quiz(
        content=content,
        pdf_file=pdf_file.filename,
        questions_number=questions_number,
        questions_type=questions_type,
        shared=False,
        user_id=current_user.public_id,
    )

    # Save the quiz to the database
    db.session.add(quiz)
    db.session.commit()


    # Return success response
    return jsonify({"message": "Quiz created successfully!","Quiz": json_content,"quiz_id": quiz.id,"download_link": quiz.pdf_file})

def share_quiz(current_user,quiz_id):
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    if not quiz:
        return jsonify({"message": "Quiz not found"})
    if quiz.user_id != current_user.public_id:
        return jsonify({"message": "You are not authorized to share this quiz"})
    if quiz.shared:
        return jsonify({"message": "Quiz already shared"})
    quiz.shared = True
    db.session.commit()
    db.session.close()
    
    return jsonify({"message": "Quiz shared successfully"})

def get_all_quizzes_of_user(current_user):
    quizs = Quiz.query.filter_by(user_id=current_user.public_id).all()
    # print(quizs)
    quiz_data = []
    for quiz in quizs:
        content = json.loads(quiz.content)
        quiz = {
            "id": quiz.id,
            "content": content,
            "pdf_file": quiz.pdf_file,
            "questions_number": quiz.questions_number,
            "questions_type": quiz.questions_type,
            "shared": quiz.shared,
            "user_id": quiz.user_id
        }
        quiz_data.append(quiz)

    return jsonify({"data": quiz_data})


def get_one_quiz_with_id(current_user,quiz_id):
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    if not quiz:
        return jsonify({"message": "Quiz not found"})
    content = json.loads(quiz.content)
    quiz = {
        "id": quiz.id,
        "content": content,
        "pdf_file": quiz.pdf_file,
        "questions_number": quiz.questions_number,
        "questions_type": quiz.questions_type,
        "shared": quiz.shared
    }
    return jsonify({"data": quiz})

def delete_one_quiz_with_id(current_user,quiz_id):
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    if not quiz:
        return jsonify({"message": "Quiz not found"})
    if quiz.user_id != current_user.public_id:
        return jsonify({"message": "You are not authorized to delete this quiz"})
    db.session.delete(quiz)
    db.session.commit()
    db.session.close()
    return jsonify({"message": "Quiz deleted successfully"})

def get_all_shared_quizzes(current_user):
    quizzes = Quiz.query.filter_by(shared=True).all()
    quizzes_data = []
    for quiz in quizzes:
        content = json.loads(quiz.content)
        quiz = {
            "id": quiz.id,
            "content": content,
            "pdf_file": quiz.pdf_file,
            "questions_number": quiz.questions_number,
            "questions_type": quiz.questions_type,
            "shared": quiz.shared,
            "user_id": quiz.user_id
        }
        quizzes_data.append(quiz)
    
    return jsonify({"data":quizzes_data})
