from flask import Blueprint, request, jsonify
from flask_mail import Message
from ..extensions import db, mail
from ..models.models import OTP, User
import random

otp_bp = Blueprint('otp', __name__)

@otp_bp.route('/check_email', methods=['POST'])
def check_email():
    data = request.get_json()
    email = data.get('email')
    user = User.query.filter_by(email=email).first()

    if user:
        return jsonify({"msg": "Email is registered"}), 200
    else:
        return jsonify({"msg": "Email is not registered"}), 404

@otp_bp.route('/send_otp', methods=['POST'])
def send_otp():
    data = request.get_json()
    email = data.get('email')
    otp_code = str(random.randint(100000, 999999))

    msg = Message('Your OTP Code', recipients=[email])
    msg.body = f"Your OTP code is {otp_code}"
    mail.send(msg)

    new_otp = OTP(email=email, otp=otp_code)
    db.session.add(new_otp)
    db.session.commit()

    return jsonify({"msg": "OTP sent successfully"}), 200

@otp_bp.route('/verify_otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    email = data.get('email')
    otp_code = data.get('otp')

    otp = OTP.query.filter_by(email=email, otp=otp_code).first()

    if otp:
        return jsonify({"msg": "OTP verified successfully"}), 200
    else:
        return jsonify({"msg": "Invalid OTP"}), 400
