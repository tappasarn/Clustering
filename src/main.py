"""
Project main file
"""
import clustering
import clustering_evaluation
import pairwise_calculation
import numpy as np
import sequence_clustering

# parameters
NUMBER_OF_CLUSTER = 6

data_seq_nozwy = []
with open('./data_seq_nozwy_1000.txt', 'r') as f:
    for i in f.readlines():
        i = i.rstrip()
        i = i.split(' ')
        if len(i)>0 and i!=['']:
            data_seq_nozwy.append(i)

data = np.array(data_seq_nozwy)
pw_original = pairwise_calculation.calculate_custom(data, 'Jaccard')

# Original
labels, medoids_row_index_init = sequence_clustering.kmedoids(data, NUMBER_OF_CLUSTER, pw_original)
print('CUSTOM orignal SSE score: ', clustering_evaluation.SSE_distances(data, labels, pw_original))
