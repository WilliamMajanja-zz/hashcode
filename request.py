class request_g():
	video_id = 0
	end_point_id = 0
	number_requests = 0

	def __init__(self, video_val, ep_val, req_val):
		self.video_id 					= video_val
		self.end_point_id 				= ep_val
		self.number_requests 			= req_val

	def get_video_id(self):
		return self.video_id

	def get_end_point_id(self):
		return self.end_point_id

	def get_number_of_requests(self):
		return self.number_requests
