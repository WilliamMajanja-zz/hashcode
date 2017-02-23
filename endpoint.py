class end_point():

	def __init__(self, get_id, latency, caches_num_val):
		self.ep_id 					= get_id
		self.latency_from_server 	= latency
		self.caches_num 			= caches_num_val
		self.reqs 					= []
		self.dict_caches = []

	def getID(self):
		return self.ep_id

	def get_lantecy_from_server(self):
		return self.latency_from_server

	def get_caches_num(self):
		return self.caches_num

	def get_caches_dict(self):
		return self.dict_caches

	def set_cache_data(self, cache_id, cache_value):
		cacheserv = {}
		cacheserv["id"] = cache_id
		cacheserv["latency"] = cache_value
		self.dict_caches.append(cacheserv)

	def num_requests(self, video):
		for elem in self.reqs:
			if int(elem.get_video_id()) == int(video):
				return [int(video), elem.get_number_of_requests()]

	def get_latency_from_request(self, cache):
		for elem in self.dict_caches:
			if int(elem["id"]) == int(cache):
				return int(elem["latency"])

	def set_cache_request(self, req):
		self.reqs.append(req)

	def calcula_ahorro(self, video, cache):
		return (int(self.get_lantecy_from_server()) - int(self.get_latency_from_request(cache))) * int(self.num_requests(video)[1])
