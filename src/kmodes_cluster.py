import numpy as np
import distance

def get_clusters(data, data_size, cluster_number, feature_size, representatives_row):
    # Get distance to medoids
    distance_arr = _get_distance_from_node_to_cluster(data, data_size, cluster_number, feature_size, representatives_row)

    # argmin return the minimum on each row
    # we can see it as cluster the node is allocated in
    return np.argmin(distance_arr, axis=1)

def _get_distance_from_node_to_cluster(data, data_size, cluster_number, feature_size, representatives_row): 
    distance_arr = np.zeros((data_size, cluster_number))

    
    for i in range(data_size):
        for j in range(cluster_number):
            distance_arr[i, j] = distance.hamming(data[i,:], representatives_row[j,:])
    return distance_arr