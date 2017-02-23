import logging
from array import array
from endpoint import end_point
from request import request_g
from cache_server import cache_server
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='(%d/%m/%Y %H:%M:%S)')
logger = logging.getLogger(__name__)


def load_file(filename):
    with open(filename) as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def generate_videos_size(input):
    mb_sizes = input[1]
    return mb_sizes.split()

def generate_end_points(config, input):
    endPointsArray = []
    last_line = 2
    id_counter = 0
    for endPointLine in range(int(config["end_points"])):
        end_point_line = input[last_line]
        ep = end_point(id_counter, end_point_line.split()[0], end_point_line.split()[1])
        for cacheData in range(int(end_point_line.split()[1])):
            ep.set_cache_data(input[last_line+cacheData+1].split()[0], input[last_line+cacheData+1].split()[1])
        endPointsArray.append(ep)
        last_line=last_line+int(end_point_line.split()[1])+1
        id_counter = id_counter+1
    return [endPointsArray, last_line]

def generate_request(config, input, line):
    request_array = []
    last_line = line
    id_counter = 0
    for request in range(int(config["req_desc"])):
        request_line = input[last_line]
        req = request_g(request_line.split()[0],request_line.split()[1],request_line.split()[2])
        request_array.append(req)
        last_line=last_line+1
        id_counter = id_counter+1
    return request_array

def generate_config(input):
    line = input[0].split()
    return {
        'videos': line[0],
        'end_points': line[1],
        'req_desc': line[2],
        'cache_servers': line[3],
        'mb_size': line[4],
    }

def update_cache(array_caches, id_cache, video, size):
    for cache_now_yes in array_caches:
        if(int(cache_now_yes.get_id())==int(id_cache)):
            print "Add video: %s in cache: %s" %(video, id_cache)
            cache_now_yes.insert_video(video, size)

def get_cache_size(caches_array_final, cache_now):
    for cache_now_yes in caches_array_final:
        if(int(cache_now_yes.get_id())==int(cache_now)):
            return cache_now_yes.get_free()

def save_problem(name, caches, array):
	f = open(name, "w")
	total_cache = 0
	for cach in caches:
		#f.write(str(cach.get_id()))
		lvs = cach.get_videos()
		if len(lvs) > 0:
			total_cache = total_cache+1

	f.write(str(total_cache))
	f.write("\n")
	for cach in array:
		if(len(cach.get_videos())>0):
			f.write(str(cach.get_id()))
			for video in cach.get_videos():
				f.write(" ")
				f.write(str(video))
		f.write("\n")


	f.close()

if __name__ == '__main__':
    logger.info('Loading data...')
    file_data   = load_file('trending_today.in')
    config      = generate_config(file_data)
    video_sizes = generate_videos_size(file_data)
    end_points  = generate_end_points(config, file_data)
    request     = generate_request(config, file_data, end_points[1])

    for req in request:
        for ep in end_points[0]:
            if int(ep.getID())==int(req.get_end_point_id()):
                ep.set_cache_request(req)

    caches_array = {}
    for eq_tmp_2 in end_points[0]:
        for cache_tmp_2 in eq_tmp_2.get_caches_dict():
            if(caches_array.has_key(int(cache_tmp_2["id"]))):
                caches_array[int(cache_tmp_2["id"])].append(eq_tmp_2)
            else:
                caches_array[int(cache_tmp_2["id"])] = [eq_tmp_2]

    caches_array_final = []
    for cache_ids in caches_array:
        caches_array_final.append(cache_server(cache_ids, config["mb_size"]))

    vp_counter = 0
    for video_tmp in video_sizes:
        cache_best_id = -1
        cache_best_value = -1
        if(int(video_tmp)<=config["mb_size"]):
            cache_sum_ahorro = {}
            for cache_now, value in caches_array.iteritems():
                if(get_cache_size(caches_array_final, cache_now)>=int(video_tmp)):
                    bestemp=0
                    for valtmp in value:
                        if(valtmp.num_requests(vp_counter)is not None):
                            if(valtmp.num_requests(vp_counter)[0]==vp_counter):
                                if (cache_best_id<0):
                                    cache_best_id = cache_now
                                    cache_best_value = valtmp.calcula_ahorro(vp_counter, cache_now)
                                else:
                                    if (cache_best_value<valtmp.calcula_ahorro(vp_counter, cache_now)):
                                        cache_best_id = cache_now
                                        cache_best_value = valtmp.calcula_ahorro(vp_counter, cache_now)
                                #print "Video: %s %s %s" % (vp_counter, cache_now, valtmp.calcula_ahorro(vp_counter, cache_now))
            update_cache(caches_array_final, cache_best_id, vp_counter, video_tmp)
        vp_counter = vp_counter + 1
    #print caches_array_final
    save_problem("salida.out", caches_array_final, caches_array_final)
