from flask import Blueprint, request, jsonify
from db import get_db_connection
import bcrypt
import jwt
import datetime
import os

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data"}), 400

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    if not bcrypt.checkpw(password.encode(), user['password'].encode()):
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode(
        {
            "user_id": user['id'],
            "email": user['email'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        os.getenv("JWT_SECRET_KEY"),
        algorithm="HS256"
    )

    return jsonify({"token": token}), 200

def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (name, email, hashed_password)
    )
    conn.commit()

    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/profile', methods=['GET'])
def profile():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({"error": "Token missing"}), 401

    try:
        decoded = jwt.decode(
            token,
            os.getenv("JWT_SECRET_KEY"),
            algorithms=["HS256"]
        )
        return jsonify({"message": "Access granted", "user": decoded}), 200

    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401

    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401
