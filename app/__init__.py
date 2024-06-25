from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt, mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from .models.models import TokenBlacklist  # Import models after initializing extensions

        @jwt.token_in_blocklist_loader
        def check_if_token_revoked(jwt_header, jwt_payload):
            jti = jwt_payload["jti"]
            token = TokenBlacklist.query.filter_by(jti=jti).first()
            return token is not None

        from .controllers import auth_controller, otp_controller
        app.register_blueprint(auth_controller.auth_bp)
        app.register_blueprint(otp_controller.otp_bp)

        db.create_all()

    return app
