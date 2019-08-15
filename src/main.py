"""
Project main file
"""
import clustering
import input_reader
import clustering_evaluation
import pairwise_calculation
from pyclustering.cluster.kmedoids import kmedoids
from sklearn.metrics import silhouette_score
import numpy as np
# parameters
NUMBER_OF_CLUSTER = 6
INPUT_FILE_PATH = '../data/data.txt'

print('intersect: ', set(np.array(['t50', 'y70', 'a30'])) & set(np.array(['t50', 'y70', 'a31'])))
print('union: ', set(np.array(['t50', 'y70', 'a30'])) | set(np.array(['t50', 'y70', 'a31'])))
# data = input_reader.read_csv_input(INPUT_FILE_PATH)
# # np.savetxt('data_bi.txt', data.astype(int), delimiter=',', fmt ='%.0f')
# t = open("data.csv", "w")
# t.write('[')
# for x in range(0, data.shape[0]):
#     for y in range(0, data.shape[1]):
#         t.write(str(data[x, y]))
#         t.write(',')
#     t.write(';')
# t.write(']')
# t.close()
# labels, final_centroids, medoids_row_index_init = clustering.kmedoids(data, NUMBER_OF_CLUSTER)
# np.savetxt('label.txt', [labels.astype(int)], delimiter=',', fmt ='%.0f')
# silhouette_avg = silhouette_score(data, labels)
# print('sse: ', clustering_evaluation.SSE_distances(data, labels, pairwise_calculation.calculate(data)))
# print('silhouette_avg for custom is: ', silhouette_avg)

# PyClustering
# kmedoids_instance = kmedoids(data, medoids_row_index_init)
# kmedoids_instance.process()
# clusters = kmedoids_instance.get_clusters()
# print('clusters: ', clusters)
# silhouette_avg = silhouette_score(data, clusters)
# print('silhouette_avg for pyclustering is: ', silhouette_avg)