"""
clustering evaluation measures library

"""
import numpy as np

def SSE_distances(data, labels, pair_wise_distances):
    
    unique_labels = np.unique(labels)
    number_of_cluster = len(unique_labels)
    
    N = len(labels)
    SSE_temp = 0
    
    for i in range(number_of_cluster):
        j = unique_labels[i]
        indices = np.where(labels == j)[0]
        
        clusters_pair_distances = pair_wise_distances[np.ix_(indices, indices)]
        SSE_temp = SSE_temp + np.sum(clusters_pair_distances)
        
    SSE_temp = SSE_temp/(N*(N-1))
    return SSE_temp

