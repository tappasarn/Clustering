"""
Project main file
"""
import clustering
import input_reader
import numpy as np

NUMBER_OF_CLUSTER = 6
INPUT_FILE_PATH = '../data/random_1000_5.txt'

data = input_reader.read_csv_input(INPUT_FILE_PATH)

# K-Medoids algorithm
labels, total_entropy, final_centroids = clustering.kmedoids(data, NUMBER_OF_CLUSTER)
print('total kmedoids entropy: ', total_entropy)

# Random
labels, total_entropy, final_centroids = clustering.randomize(data, NUMBER_OF_CLUSTER)
print('total random entropy: ', total_entropy)