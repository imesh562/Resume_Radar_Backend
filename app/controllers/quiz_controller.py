from flask import Blueprint, request, jsonify
from ..models.models import Quiz
from ..extensions import db

quiz_bp = Blueprint('quiz', __name__)


@quiz_bp.route('/quizzes', methods=['GET'])
def get_skill_based_quizzes():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('perPage', 10, type=int)
    sort = request.args.get('sort', 'created_at')

    total_count = Quiz.query.count()

    total_pages = (total_count + per_page - 1) // per_page

    quizzes = Quiz.query.order_by(db.text(sort)).paginate(page=page, per_page=per_page, error_out=False)

    quiz_list = []
    for quiz in quizzes.items:
        quiz_data = {
            'id': quiz.id,
            'title': quiz.title,
            'description': quiz.description,
            'skill': quiz.skill,
            'created_at': quiz.created_at,
        }
        quiz_list.append(quiz_data)

    response = {
        "success": True,
        "message": "Quizzes retrieved successfully",
        "data": {
            "quizzes": quiz_list,
            "page": page,
            "totalPage": total_pages,
            "totalCount": total_count
        }
    }
    return jsonify(response), 200


@quiz_bp.route('/quizzes/<int:quiz_id>/questions', methods=['GET'])
def get_quiz_questions(quiz_id):
    quiz = Quiz.query.get(quiz_id)

    if not quiz:
        return jsonify({
            "success": False,
            "message": "Quiz not found",
            "data": None
        }), 404

    questions = quiz.questions

    question_list = []
    for question in questions:
        question_data = {
            'id': question.id,
            'question_text': question.question_text,
            'options': {
                'a': question.option_a,
                'b': question.option_b,
                'c': question.option_c,
                'd': question.option_d,
            },
            'correct_answer': question.correct_answer
        }
        question_list.append(question_data)

    response = {
        "success": True,
        "message": "Questions retrieved successfully",
        "data": {
            "quiz_id": quiz.id,
            "quiz_title": quiz.title,
            "questions": question_list
        }
    }
    return jsonify(response), 200
