from flask import Flask, jsonify
from .config import Config
from .extensions import db, migrate, jwt, mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)

    @jwt.unauthorized_loader
    def unauthorized_callback(callback):
        return jsonify({
            "success": False, "message": "Missing Authorization Header", "data": None,
        }), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(callback):
        return jsonify({
            "success": False, "message": "Invalid token", "data": None,
        }), 403

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            "success": False, "message": 'Token has expired', "data": None,
        }), 403

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return jsonify({
            "success": False, "message": 'Token has been revoked', "data": None,
        }), 403

    with app.app_context():
        from .models.models import TokenBlacklist

        @jwt.token_in_blocklist_loader
        def check_if_token_revoked(jwt_header, jwt_payload):
            jti = jwt_payload["jti"]
            token = TokenBlacklist.query.filter_by(jti=jti).first()
            return token is not None

        from .controllers import auth_bp, otp_bp, quiz_bp

        app.register_blueprint(auth_bp)
        app.register_blueprint(otp_bp)
        app.register_blueprint(quiz_bp)

        db.create_all()

    return app
