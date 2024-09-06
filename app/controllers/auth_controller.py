from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash

from ..extensions import db
from ..models.models import User, TokenBlacklist

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('firstName')
    last_name = data.get('lastName')

    if User.query.filter_by(email=email).first():
        return jsonify({"success": False, "message": "Email already registered", "data": None, }), 200

    new_user = User(email=email, password_hash=generate_password_hash(password), first_name=first_name,
                    last_name=last_name)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": True, "message": "User registered successfully", "data": None, }), 200


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(
            identity={'email': email, 'user_id': user.id, 'first_name': user.first_name, 'last_name': user.last_name})
        return jsonify({
            "success": True,
            "message": "User logged in successfully",
            "data": {
                'token': access_token,
                'email': email,
                'user_id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
        }), 200

    return jsonify({"success": False, "message": "Invalid email or password", "data": None, }), 200


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    db.session.add(TokenBlacklist(jti=jti))
    db.session.commit()
    return jsonify({"success": True, "message": "User logged out", "data": None, }), 200


@auth_bp.route('/userData', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"success": True,
                    "message": "User data received successfully",
                    "data": {
                        'email': current_user['email'],
                        'user_id': current_user['user_id'],
                        'first_name': current_user['first_name'],
                        'last_name': current_user['last_name'],
                    }
                    }), 200
