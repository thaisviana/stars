from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

from star import Star

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'flask'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flask'

mongo = PyMongo(app)

@app.route('/star', methods=['GET'])
def get_all_stars():
	star = mongo.db.stars
	output = []
	for s in star.find():
		output.append(Star.jsonify(s))
	return jsonify({'result' : output})

@app.route('/star/', methods=['GET'])
def get_one_star(name):
	star = mongo.db.stars
	s = star.find_one({'name' : name})
	if s:
		return jsonify({'result' : Star.jsonify(s)})
	return jsonify({'result' : "No such name"})

@app.route('/star', methods=['POST'])
def add_star():
	star = mongo.db.stars
	
	data = Star.jsonify(request.form)
	star_id = star.insert(data)
	
	new_star = star.find_one({'_id': star_id })
	return jsonify({'result' : Star.jsonify(new_star)})

if __name__ == '__main__':
    app.run(debug=True)