"""
This module calculates clusters by using K-Mode algorithm
"""
import numpy as np
import kmodes_cluster

def calculate(data, number_of_modes): 
    # data.shape[0] return number of row
    # data.shape[1] return number of columns
    data_size, feature_size = data.shape

    if number_of_modes > data_size:
        raise Exception('Number of modes is more than data size')

    # Select ramdom indices for initial representation object == number_of_medoids
    modes_row_index_init = np.random.choice(data_size, number_of_modes, replace=False)
    modes_row_init = data[modes_row_index_init,:]
    # medoids_row_index_init = np.array([426, 550, 515, 9, 432, 854])

    clusters = kmodes_cluster.get_clusters(data, data_size, number_of_modes, feature_size, modes_row_init)

    # Find new medoids from the clusters until medoids do not change any more
    modes_row_prev = modes_row_init
    modes_row_current = np.full((number_of_modes, feature_size), -1)

    while not np.array_equal(modes_row_prev, modes_row_current):
        # If they are not the same CURRENT becomes PREV
        modes_row_prev = np.copy(modes_row_current)

        # Find new current
        for i in range(number_of_modes):
            # Get index where value is equal to i
            # .where returns tuple so we need [0] here
            indices = np.where(clusters == i)[0]
            
            cluster_data = data[indices,:]
            for j in range(feature_size):
                counts = np.bincount(cluster_data[:,j])
                modes_row_current[i,j] = np.argmax(counts)

        # We have new medoids
        # Get new clusters
        clusters = kmodes_cluster.get_clusters(data, data_size, number_of_modes, feature_size, modes_row_current)
        
    return (clusters, modes_row_current)

