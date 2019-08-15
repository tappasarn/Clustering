"""
This is the entry module of the clustering library

This contains all clustering methods APIs that currently have been implemented in this library
"""
import entropy
import kmedoids_core
import randomize_core
import kmodes_core
import khistograms_core

def kmedoids(data, NUMBER_OF_CLUSTER):
    labels, final_medoids = kmedoids_core.calculate(data, NUMBER_OF_CLUSTER)
    return (labels, final_medoids)

def randomize(data, NUMBER_OF_CLUSTER):
    labels = randomize_core.calculate(data, NUMBER_OF_CLUSTER)    
    return (labels, None)

def kmodes(data, NUMBER_OF_CLUSTER):
    labels, final_mode = kmodes_core.calculate(data, NUMBER_OF_CLUSTER)
    return (labels, final_mode)

def khistograms(data, NUMBER_OF_CLUSTER):
    labels, final_histogram = khistograms_core.calculate(data, NUMBER_OF_CLUSTER)
    return (labels, final_histogram)