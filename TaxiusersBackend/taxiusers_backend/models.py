from sqlalchemy import func
from taxiusers_backend.db import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(250))
    lastLoginAt = db.Column(db.DateTime, nullable=True)
    createdAt = db.Column(db.DateTime, server_default=func.now())

    # superadmin: 1, admin: 2, drivers: 3, riders/passengers: 4
    role = db.Column(db.Integer, nullable=False, default=4)

    def __init__(self, username, password, role, createdAt):
        self.username = username
        # Hash and Salt Password
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
        self.role = role
        self.createdAt = createdAt
