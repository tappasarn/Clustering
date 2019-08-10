import numpy as np

def get_cluster(data, data_size, number_of_histogram, feature_size, histogram_current):
    # Get distance to medoids
    distance_arr = _get_distance_from_node_to_medoids(data, data_size, number_of_histogram, feature_size, histogram_current)
	
	# argmin return the minimum on each row
	# we can see it as cluster the node is allocated in
    return np.argmin(distance_arr, axis=1)

def _get_distance_from_node_to_medoids(data, data_size, number_of_histogram, feature_size, histogram_current): 
	distance_arr = np.zeros((data_size, number_of_histogram))
	for i in range(data_size):
		for k in range(number_of_histogram):
			total_k_histogram_distance = 0
			for j in range(feature_size):
				current_data = data[i, j]
				histogram_cur = histogram_current[k][j, :]
				histogram_sum = np.sum(histogram_cur)
				if(histogram_sum == 0):
					raise Exception('no active histogram')
				distance = (histogram_sum - histogram_cur[current_data]) / histogram_sum
				
				total_k_histogram_distance = total_k_histogram_distance + distance

			distance_arr[i, k] = total_k_histogram_distance
	return distance_arr