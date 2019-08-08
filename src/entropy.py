"""
This module is use for entropy calculation
"""
import numpy as np
import math

def calculate_entropy_simple(data, labels):
    number_of_features = data.shape[1]
    unique_labels = np.unique(labels)
    number_of_cluster = len(unique_labels)

    total_entropy = 0

    # Calculate entropy as sum of the entrpies for each feature in a cluster
    # and sum of the entropies of the clusters
    cluster_entropies = np.zeros((1, number_of_cluster))

    for i in range(number_of_cluster):
        j = unique_labels[i]
        idx = np.where(labels == j)[0]
        data_cluster = data[idx, :]

        for j in range(number_of_features):
                temp = data_cluster[: , j]
                n = len(temp)
                unique_vals = np.unique(temp)

                for k in range(len(unique_vals)):
                    m = len(np.where(temp == unique_vals[k]))
                    p = m/n
                    cluster_entropies[i] = cluster_entropies[i] - p * math.log(p)
						
	for i in range(number_of_cluster):
		total_entropy = total_entropy + cluster_entropies[i]
	
	return total_entropy