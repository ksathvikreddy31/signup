from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from database import init_db, db
from models import User
from flask_cors import CORS

app = Flask(__name__)

# ✅ FIXED: Apply CORS AFTER app creation
CORS(app)

# 🔥 Initialize DB
init_db(app)

# 🚀 Create tables
with app.app_context():
    db.create_all()

# ✅ Signup Route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json

    print("Received:", data)  # 🔍 DEBUG LINE

    existing_user = User.query.filter_by(email=data['email']).first()

    if existing_user:
        return jsonify({"error": "Email already exists"}), 400

    hashed_password = generate_password_hash(data['password'])

    new_user = User(
        name=data['name'],
        email=data['email'],
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})


if __name__ == "__main__":
    app.run(debug=True)