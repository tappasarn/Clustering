"""
This module is use for entropy calculation
"""
import numpy as np
import math

def calculate_entropy_simple(data, labels):
    # commented code here is to traform python numpy array to matlab array for testing purpose 
    # t = open("data.csv", "w")
    # t.write('[')
    # for x in range(0, data.shape[0]):
    #     for y in range(0, data.shape[1]):
    #         t.write(str(data[x, y]))
    #         t.write(', ')
    #     t.write(';')
    # t.write(']')
    # t.close()

    # f = open("label.csv", "w")
    # f.write('[')
    # for i in labels:
    #     f.write(str(i))
    #     f.write(', ')
    # f.write(']')
    # f.close()
    
    number_of_features = data.shape[1]
    unique_labels = np.unique(labels)
    number_of_cluster = len(unique_labels)

    total_entropy = 0

    # Calculate entropy as sum of the entrpies for each feature in a cluster
    # and sum of the entropies of the clusters
    cluster_entropies = np.zeros(number_of_cluster)

    for i in range(number_of_cluster):
        j = unique_labels[i]
        idx = np.where(labels == j)
        data_cluster = data[idx[0], :]

        for j in range(number_of_features):
            temp = data_cluster[: , j]
            n = len(temp)
            unique_vals = np.unique(temp)

            for k in range(len(unique_vals)):
                m = len(np.where(temp == unique_vals[k])[0])
                p = m/n
                cluster_entropies[i] = cluster_entropies[i] - p * math.log(p)
    for i in range(number_of_cluster):
        total_entropy = total_entropy + cluster_entropies[i]

    return total_entropy