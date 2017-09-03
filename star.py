class Star():
	def __init__(self, name=None, distance=None,star_id=None):
		self.name = name
		self.distance = distance
		self.star_id = star_id
	
	def jsonify(obj):
		name = obj['name']
		distance = obj['distance']
		return {'name': name, 'distance': distance}