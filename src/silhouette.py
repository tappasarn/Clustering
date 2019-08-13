"""
This module is used for silhouette silhouette coefficient calculation
"""
import numpy as np
import pairwise_calculation
import random
from sklearn.metrics import silhouette_samples, silhouette_score

def calculate(data, clusters):
    # avg = silhouette_score(data, clusters)
    # each = silhouette_samples(data, clusters)
    calculate_custom_each(data, clusters)
    return 0

def calculate_custom_each(data, clusters):
    pw = pairwise_calculation.calculate_custom(data, 'Jaccard')

    # Contains mean distances for each data to all of other members
    # in the SAME cluster
    internal_mean_distance_each = np.full(data.shape[0], -1, dtype='float')

    # Contains mean distance of each sample to all points in any other cluster, 
    # of which the sample is not a member
    external_mean_distance_each = np.full(data.shape[0], -1, dtype='float')

    # loop over clusters
    for i in range(len(clusters)):
        cluster_i_idx = np.where(clusters == i)[0]
        # cluster_i = data[cluster_i_idx, :]
        clusters_pw = pw[np.ix_(cluster_i_idx, cluster_i_idx)]

        # loop over cluster members
        for j in range(len(cluster_i_idx)):
            # -1 here is to exclude the distance to itself which is always 0
            mean_val = np.mean(clusters_pw[j, :])
            # mean_val = np.sum(clusters_pw[j, :]) / (len(cluster_i_idx) - 1 )
            internal_mean_distance_each[cluster_i_idx[j]] = mean_val
        
            # randomly select any cluster that data-j is not a member of 
            if i == 0: 
                numbers = range(1, len(clusters))
            elif i == len(clusters) - 1:
                numbers = range(1, len(clusters) - 1)
            else:

                numbers = list(range(0,i)) + list(range(i + 1, len(clusters)))
            random_cluster_idx = random.choice(numbers)

            print('i is: ', i)
            print('random is: ', random_cluster_idx)
        # print('internal_mean_distance_each: ', internal_mean_distance_each)



def calculate_custom_avg(data, clusters):
    print('cal')