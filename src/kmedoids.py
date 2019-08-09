"""
This module job is to calculate K-Medoids

K-Medoids uses 'K' MOST CENTRALLY LOCATED object as reference points
"""
import input_reader
import numpy as np
import cluster
import pairwise_calculation
from sklearn.metrics.pairwise import pairwise_distances

def calculate(data, number_of_medoids): 
    # data.shape[0] return number of row
    # data.shape[1] return number of columns
    data_size, feature_size = data.shape

    # crate pair wise table so we will not have to do it all the time
    pair_wise_distance = pairwise_calculation.calculate(data)

    if number_of_medoids > data_size:
        raise Exception('Number of medoids is more than data size')

    # Select ramdom indices for initial representation object == number_of_medoids
    medoids_row_index_init = np.random.choice(data_size, number_of_medoids, replace=False)
    # medoids_row_index_init = np.array([426, 550, 515, 9, 432, 854])

    clusters = cluster.get_cluster(data, data_size, number_of_medoids, feature_size, medoids_row_index_init, pair_wise_distance)

    # Find new medoids from the clusters until medoids do not change any more
    medoids_row_index_prev = medoids_row_index_init
    medoids_row_index_current = np.full(number_of_medoids, -1)

    while not np.array_equal(medoids_row_index_prev, medoids_row_index_current):
        # If they are not the same CURRENT becomes PREV
        medoids_row_index_prev = np.copy(medoids_row_index_current)

        # Find new current
        for i in range(number_of_medoids):
            # Get index where value is equal to i
            # .where returns tuple so we need [0] here
            indices = np.where(clusters == i)[0]

            # Find new medoids
            # Get pair distance for the indices
            clusters_pair_distance_arr = pair_wise_distance[np.ix_(indices, indices)]

            # find the index of minimum mean row
            min_sum_index = np.argmin(np.mean(clusters_pair_distance_arr,axis=1))
            medoids_row_index_current[i] = indices[min_sum_index]

        # We have new medoids
        # Get new clusters
        clusters = cluster.get_cluster(data, data_size, number_of_medoids, feature_size, medoids_row_index_current, pair_wise_distance)
        
    return (clusters, medoids_row_index_current)

