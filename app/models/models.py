from datetime import datetime, timedelta

from ..extensions import db


class TokenBlacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class OTPRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def can_send_otp(email):
        one_hour_ago = datetime.utcnow() - timedelta(hours=1)
        requests = OTPRequest.query.filter_by(email=email).filter(OTPRequest.timestamp > one_hour_ago).all()
        return len(requests) < 5

    @staticmethod
    def time_until_next_allowed(email):
        one_hour_ago = datetime.utcnow() - timedelta(hours=1)
        requests = OTPRequest.query.filter_by(email=email).filter(OTPRequest.timestamp > one_hour_ago).all()
        if len(requests) < 5:
            return 0
        first_request = requests[0]
        time_until_next = first_request.timestamp + timedelta(hours=1) - datetime.utcnow()
        return time_until_next.total_seconds()


class OTPCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    otp_code = db.Column(db.String(6), nullable=False)
    expiration_time = db.Column(db.DateTime, nullable=False)
