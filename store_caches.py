from cache_server import cache_server

def save_problem(name, caches):

	f = open(name, "w")
	f.write(len(caches))
	f.write("\n")

	for cach in caches:
		f.write(str(cach.get_id()))
			for lvs in cach.get_videos():
				if len(lvs) > 0:
					for v in lvs:
						f.write(" " + str(v))
		f.write("\n")

	f.close()
