"""
This is the entry module of the clustering library

This contains all clustering methods APIs that currently have been implemented in this library
"""
import entropy
import kmedoids_core
import randomize_core
import kmodes_core
import khistograms_core
import silhouette

def kmedoids(data, NUMBER_OF_CLUSTER):
    labels, final_medoids = kmedoids_core.calculate(data, NUMBER_OF_CLUSTER)
    # total_entropy = entropy.calculate_entropy_simple(data, labels)
    sc = silhouette.calculate(data, labels)

    return (labels, 0, final_medoids, sc)

def randomize(data, NUMBER_OF_CLUSTER):
    labels = randomize_core.calculate(data, NUMBER_OF_CLUSTER)
    total_entropy = entropy.calculate_entropy_simple(data, labels)
    sc = silhouette.calculate(data, labels)

    return (labels, total_entropy, None, sc)

def kmodes(data, NUMBER_OF_CLUSTER):
    labels, final_mode = kmodes_core.calculate(data, NUMBER_OF_CLUSTER)
    total_entropy = entropy.calculate_entropy_simple(data, labels)
    sc = silhouette.calculate(data, labels)

    return (labels, total_entropy, final_mode, sc)

def khistograms(data, NUMBER_OF_CLUSTER):
    labels, final_histogram = khistograms_core.calculate(data, NUMBER_OF_CLUSTER)
    total_entropy = entropy.calculate_entropy_simple(data, labels)
    sc = silhouette.calculate(data, labels)

    return (labels, total_entropy, final_histogram, sc)  

