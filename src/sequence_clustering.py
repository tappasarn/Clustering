"""
This is the entry module of the clustering library

This contains all clustering methods APIs that currently have been implemented in this library
"""
import numpy as np

def kmedoids(data, nClusters, pair_wise_distances):
    # data.shape[0] return number of row
    # data.shape[1] return number of columns
    data_size = data.shape[0]
    
    if nClusters > data_size:
        raise Exception('Number of medoids is more than data size')

    # Select ramdom indices for initial representation object == number_of_medoids
    #medoids_row_index_init = np.random.choice(data_size, nClusters, replace=False)
    labels = np.random.randint(0, nClusters, data_size) # random clustering
    
    medoids_row_index_init = []
    # calculate medoids
    for i in range(nClusters):
        indices = np.where(labels == i)[0]
        clusters_pair_distance_arr = pair_wise_distances[np.ix_(indices, indices)]
        max_sum_index = np.argmin(np.mean(clusters_pair_distance_arr,axis=1))
        medoids_row_index_init.append(indices[max_sum_index])

    medoids_row_index_init = np.array(medoids_row_index_init)
    print(medoids_row_index_init)
    
    #labels = kmedoids_get_cluster(data, data_size, nClusters, medoids_row_index_init, pair_wise_distances)

    # Find new medoids from the clusters until medoids do not change any more
    medoids_row_index_prev = medoids_row_index_init
    medoids_row_index_current = np.full(nClusters, -1)

    j = 0
    while not np.array_equal(medoids_row_index_prev, medoids_row_index_current):
        # If they are not the same CURRENT becomes PREV
        medoids_row_index_prev = np.copy(medoids_row_index_current)

        # Find new current
        for i in range(nClusters):
            # Get index where value is equal to i
            # .where returns tuple so we need [0] here
            indices = np.where(labels == i)[0]
            
            # Find new medoids
            # Get pair distance for the indices
            clusters_pair_distance_arr = pair_wise_distances[np.ix_(indices, indices)]

            # find the index of minimum mean row
            max_sum_index = np.argmin(np.mean(clusters_pair_distance_arr,axis=1))
            medoids_row_index_current[i] = indices[max_sum_index]

        # We have new medoids
        # Get new clusters
        labels = kmedoids_get_cluster(data, data_size, nClusters, medoids_row_index_current, pair_wise_distances)
        j = j + 1

    print('Number of iterations = ', j)        
    return (labels, medoids_row_index_init)

def kmedoids_get_cluster(input_arr, data_size, medoids_number, medoids_row_idx, pair_wise_distances):
    # Get distance to medoids
    distance_arr = np.zeros((data_size, medoids_number))

    for i in range(data_size):
        for j in range(medoids_number):
            distance_arr[i, j] = pair_wise_distances[i, medoids_row_idx[j]]

    # argmin return the minimum on each row
    # we can see it as cluster the node is allocated in
    return np.argmin(distance_arr, axis=1)
