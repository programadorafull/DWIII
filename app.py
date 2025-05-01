from flask import Flask, jsonify, request
from decorators.auth import require_auth
from models.user_factory import UserFactory
from observers.subject import Subject
from observers.email_notifier import EmailNotifier
from observers.log_notifier import LogNotifier
from models.database_singleton import DatabaseConnection

app = Flask(__name__)

# Setup de Observers
subject = Subject()
subject.register(EmailNotifier())
subject.register(LogNotifier())

@app.route('/')
def home():
    return "Bem-vindo à WebApp com Design Patterns!"

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    user = UserFactory.create_user(data['type'], data['name'])
    return jsonify({"name": user.name, "role": user.role})

@app.route('/add_pet', methods=['POST'])
def add_pet():
    data = request.json
    pet_name = data['name']
    subject.notify_all(pet_name)
    return jsonify({"message": f"Pet {pet_name} cadastrado com sucesso!"})

@app.route('/db', methods=['GET'])
def db_connection():
    db = DatabaseConnection()
    return jsonify({"db_status": db.get_connection()})

@app.route('/protected', methods=['GET'])
@require_auth
def protected():
    return jsonify({"message": "Você acessou uma rota protegida!"})

if __name__ == '__main__':
    app.run(debug=True)
