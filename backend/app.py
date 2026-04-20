from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # Importante para que el frontend pueda hablar con el backend

# Configuración de la base de datos (conecta con Docker)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Workshop(db.Model):
    __tablename__ = 'workshops'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))
    place = db.Column(db.String(100))
    category = db.Column(db.String(50))

@app.route('/workshops', methods=['GET'])
def get_workshops():
    workshops = Workshop.query.all()
    output = []
    for w in workshops:
        output.append({'id': w.id, 'name': w.name, 'description': w.description, 'date': str(w.date), 'time': str(w.time), 'place': w.place, 'category': w.category})
    return jsonify(output)

@app.route('/workshops', methods=['POST'])
def add_workshop():
    data = request.json
    new_workshop = Workshop(name=data['name'], description=data['description'], date=data['date'], time=data['time'], place=data['place'], category=data['category'])
    db.session.add(new_workshop)
    db.session.commit()
    return jsonify({'message': 'Taller creado'}), 201

@app.route('/workshops/<int:id>', methods=['DELETE'])
def delete_workshop(id):
    workshop = Workshop.query.get(id)
    db.session.delete(workshop)
    db.session.commit()
    return jsonify({'message': 'Taller eliminado'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
