import random
from datetime import datetime, timedelta

from flask import Blueprint
from flask import current_app, jsonify, request
from flask_mail import Message

from ..extensions import db, mail
from ..models.models import OTPRequest, OTPCode
from ..models.models import User

otp_bp = Blueprint('otp', __name__)


@otp_bp.route('/check_email', methods=['POST'])
def check_email():
    data = request.get_json()
    email = data.get('email')
    user = User.query.filter_by(email=email).first()

    if user:
        return jsonify({"success": False, "message": "Email is registered", "data": None, }), 200
    else:
        return jsonify({"success": True, "message": "Email is not registered", "data": None, }), 200


@otp_bp.route('/send_otp', methods=['POST'])
def send_otp():
    data = request.get_json()
    email = data.get('email')

    if not OTPRequest.can_send_otp(email):
        time_remaining = OTPRequest.time_until_next_allowed(email)
        return jsonify({
            "success": False,
            "message": f"You have to wait {int(time_remaining / 60)} minutes before requesting another OTP",
            "data": None
        }), 200

    otp_code = random.randint(100000, 999999)

    msg = Message('Your OTP Code', sender=current_app.config['MAIL_DEFAULT_SENDER'], recipients=[email])
    msg.body = f'Your OTP code is {otp_code}. It is valid for 5 minutes.'
    mail.send(msg)

    new_request = OTPRequest(email=email)
    new_otp_code = OTPCode(email=email, otp_code=otp_code, expiration_time=datetime.utcnow() + timedelta(minutes=5))
    db.session.add(new_request)
    db.session.add(new_otp_code)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "OTP sent successfully",
        "data": None,
    }), 200


@otp_bp.route('/verify_otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    email = data.get('email')
    otp_code = data.get('otp')

    otp_record = OTPCode.query.filter_by(email=email, otp_code=otp_code).first()

    if otp_record and otp_record.expiration_time > datetime.utcnow():
        return jsonify({
            "success": True,
            "message": "OTP verified successfully",
            "data": None
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Invalid or expired OTP",
            "data": None
        }), 200
