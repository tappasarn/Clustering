"""
This module is use for entropy calculation
"""
import numpy as np

def calculate_entropy_simple(data, nCategories, labels):
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

