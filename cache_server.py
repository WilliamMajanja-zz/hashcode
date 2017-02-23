from endpoint import end_point

class cache_server():

	def __init__(self, id_val, tam):
		self.id = id_val
		self.tam = int(tam)
		self.free = int(tam)
		self.videos = []
		self.end_points = []

	def get_free(self):
		return self.free

	def get_tam(self):
		return self.tam

	def get_id(self):
		return self.id

	def get_videos(self):
		#print self.videos
		return self.videos

	def insert_video(self, video, size):
		if int(size) > int(self.get_tam()):
			return False
		else:
			self.videos.append(video)
			self.free -= int(size)
			return True
