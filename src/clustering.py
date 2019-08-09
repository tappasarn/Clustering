"""
This is the entry module of the clustering library

This contains all clustering methods APIs that currently have been implemented in this library
"""
import entropy
import kmedoids_core
import randomize_core

def kmedoids(data, NUMBER_OF_CLUSTER):
    labels, final_medoids = kmedoids_core.calculate(data, NUMBER_OF_CLUSTER)
    total_entropy = entropy.calculate_entropy_simple(data, labels)

    return (labels, total_entropy, final_medoids)

def randomize(data, NUMBER_OF_CLUSTER):
    labels = randomize_core.calculate(data, NUMBER_OF_CLUSTER)
    total_entropy = entropy.calculate_entropy_simple(data, labels)

    return (labels, total_entropy, None)

