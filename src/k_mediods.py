"""
This module job is to calculate K-mediods

K-mediods uses 'K' MOST CENTRALLY LOCATED object as reference points
"""
import input_reader
import numpy as np
import cluster
import pairwise_calculation
from sklearn.metrics.pairwise import pairwise_distances

# Constant for number of mediods
# If you want to change number of mediods, do it here.
MEDIODS_NUMBER = 2

input_arr = input_reader.read_csv_input('')

# input_arr.shape[0] return number of row
# input_arr.shape[1] return number of columns
data_size, feature_size = input_arr.shape

# crate pair wise table so we will not have to do it all the time
pair_wise_distance = pairwise_calculation.calculate(input_arr)

if MEDIODS_NUMBER > data_size:
    raise Exception('Number of mediods is more than data size')

# Select ramdom indices for initial representation object == mediods_number
mediods_row_index_init = np.random.choice(data_size, MEDIODS_NUMBER, replace=False)
# mediods_row_index_init = np.array([196, 244])

clusters = cluster.get_cluster(input_arr, data_size, MEDIODS_NUMBER, feature_size, mediods_row_index_init, pair_wise_distance)

# Find new mediods from the clusters until mediods do not change any more
mediods_row_index_prev = mediods_row_index_init
mediods_row_index_current = np.full(MEDIODS_NUMBER, -1)

while not np.array_equal(mediods_row_index_prev, mediods_row_index_current):
    # If they are not the same CURRENT becomes PREV
    mediods_row_index_prev = np.copy(mediods_row_index_current)

    # Find new current
    for i in range(MEDIODS_NUMBER):
        # Get index where value is equal to i
        # .where returns tuple so we need [0] here
        indices = np.where(clusters == i)[0]

        # Find new mediods
        # Get pair distance for the indices
        clusters_pair_distance_arr = pair_wise_distance[np.ix_(indices, indices)]

        # find the index of minimum mean row
        min_sum_index = np.argmin(np.mean(clusters_pair_distance_arr,axis=1))
        mediods_row_index_current[i] = indices[min_sum_index]

    # We have new mediods
    # Get new clusters
    clusters = cluster.get_cluster(input_arr, data_size, MEDIODS_NUMBER, feature_size, mediods_row_index_current, pair_wise_distance)
    
print('final mediods: ', mediods_row_index_current)

result = []
for i in range(MEDIODS_NUMBER):
    result.append(np.where(clusters == i)[0])

file = open('cluster_members_idx.txt', 'w')
for line in result:
    file.write(",".join([str(x) for x in line]))
    file.write('\n')
file.close()

