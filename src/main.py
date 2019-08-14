"""
Project main file
"""
import clustering
import input_reader
import pairwise_calculation
import clustering_evaluation
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import numpy as np

import time
# parameters
start_time = time.time()

NUMBER_OF_CLUSTER = 6
CLUSTEING_METHOD = 'KHISTOGRAMS'
INPUT_FILE_PATH = '../data/data.txt'

data, features = input_reader.read_csv_input(INPUT_FILE_PATH)

compressed_data = np.packbits(data, axis = 1)

# test 1000 result
for i in range(data.shape[0]):
    if not np.array_equal(np.unpackbits(compressed_data[i, :])[0: features.shape[0]], data[i, :]):
        print('i is: ', i)
        print('unpack: ', np.unpackbits(compressed_data[i, :])[0: features.shape[0]])
        print('actual: ', data[i, :])
        raise Exception('wrong !')

# pw_dis = pairwise_calculation.calculate_custom(data, 'Jaccard')

# print('pw_dis done')

# labels, final_centroids = clustering.kmedoids(data, NUMBER_OF_CLUSTER)
# sse_dis = clustering_evaluation.SSE_distances(data, labels, pw_dis)
# #sc_score = silhouette_score(pw_dis, labels, metric="precomputed")

# print('total kmedoids SSE: ', sse_dis)
# #print('avg kmedoids silhouette coefficient: ', sc_score)
# print('==============================')

# labels, final_centroids = clustering.randomize(data, NUMBER_OF_CLUSTER)
# sse_dis = clustering_evaluation.SSE_distances(data, labels, pw_dis)
# #sc_score = silhouette_score(pw_dis, labels, metric="precomputed")

# print('total random SSE: ', sse_dis)
# # print('avg random silhouette coefficient: ', sc_score)
# print('==============================')

# clusterer = KMeans(n_clusters=NUMBER_OF_CLUSTER, random_state=10)
# labels = clusterer.fit_predict(data)
# sse_dis = clustering_evaluation.SSE_distances(data, labels, pw_dis)
# # sc_score = silhouette_score(pw_dis, labels, metric="precomputed")

# print('total kmean SSE: ', sse_dis)
# # print('avg kmean silhouette coefficient: ', sc_score)
# print('==============================')
# print("--- %s seconds ---" % (time.time() - start_time))

# # labels, final_centroids = clustering.kmodes(data, NUMBER_OF_CLUSTER)
# # sse_dis = clustering_evaluation.SSE_distances(data, labels, pw_dis)
# # sc_score = silhouette_score(pw_dis, labels, metric="precomputed")

# # print('total kmode SSE: ', sse_dis)
# # print('avg kmode silhouette coefficient: ', sc_score)
# # print('==============================')

# # labels, final_centroids = clustering.khistograms(data, NUMBER_OF_CLUSTER) 
# # sse_dis = clustering_evaluation.SSE_distances(data, labels, pw_dis)
# # sc_score = silhouette_score(pw_dis, labels, metric="precomputed")

# # print('total khistograms SSE: ', sse_dis)
# # print('avg khistograms silhouette coefficient: ', sc_score)
# # print('==============================')