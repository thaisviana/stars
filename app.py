from flask import Flask
from flask_cors import CORS, cross_origin
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

from student import Student

app = Flask(__name__)
ors = CORS(app)
app.config.from_object('config.Config')

mongo = PyMongo(app)



@app.route('/student/<anonymous_id>', methods=['GET'])
@cross_origin()
def get_one(anonymous_id):
    try:
        signature = request.headers['X-Hub-Signature']
    except:
        signature = None
    auth = Student.compare_signature(signature)
    if auth:
        student = mongo.db.heroku_v7l9xvr5
        s = student.find_one({'anonymous_id': anonymous_id})
        if s:
            return jsonify({'result': Student.jsonify(s)})
        return jsonify({'result': "No such anonymous_id"})
    else:
        return jsonify({'result': 'gtfo'})


@app.route('/student', methods=['POST'])
@cross_origin()
def add():
    try:
        signature = request.headers['X-Hub-Signature']
    except:
        signature = None
    auth = Student.compare_signature(signature)
    if auth:
        student = mongo.db.heroku_v7l9xvr5

        s = student.find_one({'anonymous_id': request.json['anonymous_id']})
        if not s:
            data = Student.jsonify(request.json)
            student_id = student.insert(data)
            new_student = student.find_one({'_id': student_id})
            return jsonify({'result': Student.jsonify(new_student)})
        else:
            new_data = Student.jsonify(request.json)
            student.update({"anonymous_id": request.json['anonymous_id']}, new_data)
            s = student.find_one({'anonymous_id': request.json['anonymous_id']})
            return jsonify({'result': Student.jsonify(s)})
    else:
        return jsonify({'result': 'gtfo'})


# @app.route('/student/<anonymous_id>', methods=['PATCH'])
# @cross_origin()
# def update(anonymous_id):
#     student = mongo.db.heroku_v7l9xvr5
#     data = Student.jsonify(request.json)
#     s = student.update({"anonymous_id": anonymous_id}, data)
#     print(s)
#     if s:
#         return jsonify({'result': s})
#     return jsonify({'result': 'Error'})


if __name__ == '__main__':
    app.run(debug=False)
