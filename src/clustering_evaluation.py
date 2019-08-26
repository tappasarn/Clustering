"""
clustering evaluation measures library

"""
import numpy as np

def SSE_distances(data, labels, pair_wise_distances):
    
    unique_labels = np.unique(labels)
    number_of_cluster = len(unique_labels)
    
    SSE_clusters = np.zeros(number_of_cluster)
    SSE_temp = 0
    
    for i in range(number_of_cluster):
        j = unique_labels[i]
        indices = np.where(labels == j)[0]
        cluster_size = len(indices)
        
        clusters_pair_distances = pair_wise_distances[np.ix_(indices, indices)]
        power_two = np.power(clusters_pair_distances, 2)
        SSE_temp = SSE_temp + np.sum(power_two) / cluster_size / 2
        
    return SSE_temp


