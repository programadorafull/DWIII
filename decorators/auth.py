from functools import wraps
from flask import request, jsonify
from config import SECRET_KEY

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token != f"Bearer {SECRET_KEY}":
            return jsonify({"error": "Não autorizado"}), 401
        return f(*args, **kwargs)
    return decorated
