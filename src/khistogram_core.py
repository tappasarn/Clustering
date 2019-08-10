"""
This module calculates clusters by using K-Histogram algorithm
"""
import numpy as np
import khistogram_cluster
import randomize_core

def _get_data_per_cluster(cluster_idx, clusters, data):
    i_cluster_row_idx = np.where(clusters == cluster_idx)[0]
    return data[i_cluster_row_idx, :]

def _get_histogram(number_of_histogram, clusters, data, feature_size):
    histograms = []
    for i in range(number_of_histogram):
        cluster_i_data = _get_data_per_cluster(i, clusters, data)
        cluster_histogram = np.zeros((feature_size, np.amax(data) + 1))

        for j in range(feature_size):
            cluster_histogram[j, :] = np.bincount(cluster_i_data[:,j], minlength = np.amax(data)+1)
            if len(np.where(cluster_histogram[j, :] == 0)[0]) == np.amax(data) + 1:
                raise Exception('bit count return all 0')
        histograms.append(cluster_histogram)
    return histograms

def _are_equal(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    
    result = False
    for i in range(len(list_1)):
        if np.array_equal(list_1[i], list_2[i]):
            result = True
        else:
            result = False
    return result

def calculate(data, number_of_histogram): 
    # data.shape[0] return number of row
    # data.shape[1] return number of columns
    data_size, feature_size = data.shape

    if number_of_histogram > data_size:
        raise Exception('Number of modes is more than data size')

    # Randomly create cluster
    clusters = randomize_core.calculate(data, number_of_histogram)

    # Create histogram init
    histograms = _get_histogram(number_of_histogram, clusters, data, feature_size)

    # Find new histogram from the clusters until histogram do not change any more
    histogram_prev = []
    histogram_current = histograms
    while not _are_equal(histogram_prev, histogram_current):
        # re-cluster
        clusters = khistogram_cluster.get_cluster(data, data_size, number_of_histogram, feature_size, histogram_current)
        histogram_prev = histogram_current
        histogram_current = _get_histogram(number_of_histogram, clusters, data, feature_size)
    
    return (clusters, histogram_current)
