```python
from database import database_connection, QuizSchema
from user import current_user

def create_quiz(quiz_title, quiz_questions):
    quiz = QuizSchema()
    quiz.title = quiz_title
    quiz.questions = quiz_questions
    quiz.creator = current_user

    database_connection.session.add(quiz)
    database_connection.session.commit()

    return quiz

def get_quiz(quiz_id):
    quiz = database_connection.session.query(QuizSchema).filter_by(id=quiz_id).first()
    return quiz

def update_quiz(quiz_id, quiz_title=None, quiz_questions=None):
    quiz = get_quiz(quiz_id)
    if quiz_title:
        quiz.title = quiz_title
    if quiz_questions:
        quiz.questions = quiz_questions

    database_connection.session.commit()

    return quiz

def delete_quiz(quiz_id):
    quiz = get_quiz(quiz_id)
    database_connection.session.delete(quiz)
    database_connection.session.commit()

def answer_quiz(quiz_id, user_answers):
    quiz = get_quiz(quiz_id)
    if quiz:
        quiz.answers[current_user] = user_answers
        database_connection.session.commit()

    return quiz
```