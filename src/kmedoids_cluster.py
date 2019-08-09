import numpy as np

def get_cluster(input_arr, data_size, medoids_number, feature_size, medoids_row_idx, pair_wise_distance):
    # Get distance to medoids
    distance_arr = _get_distance_from_node_to_medoids(data_size, medoids_number, pair_wise_distance, feature_size, medoids_row_idx)

    # argmin return the minimum on each row
    # we can see it as cluster the node is allocated in
    return np.argmin(distance_arr, axis=1)

def _get_distance_from_node_to_medoids(data_size, medoids_number, pair_wise_distance, feature_size, medoids_row_idx): 
    distance_arr = np.zeros((data_size, medoids_number))

    for i in range(data_size):
        for j in range(medoids_number):
            distance_arr[i, j] = pair_wise_distance[i, medoids_row_idx[j]]  
    return distance_arr