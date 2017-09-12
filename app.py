from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

from student import Student

app = Flask(__name__)

mongo = PyMongo(app)
app.config.from_object('config.Config')

@app.route('/student', methods=['GET'])
def get_all():
    student = mongo.db.student
    output = []
    for s in student.find():
        output.append(Student.jsonify(s))
    return jsonify({'result': output})

@app.route('/student/', methods=['GET'])
def get_one(student_id):
    student = mongo.db.student
    s = student.find_one({'student_id': student_id})
    if s:
        return jsonify({'result': Student.jsonify(s)})
    return jsonify({'result': "No such name"})

@app.route('/student', methods=['POST'])
def add():
    student = mongo.db.student

    data = Student.jsonify(request.form)
    student_id = student.insert(data)

    new_student = student.find_one({'_id': student_id })
    return jsonify({'result': Student.jsonify(new_student)})

if __name__ == '__main__':
    app.run(debug=False)
