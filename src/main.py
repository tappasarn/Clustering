"""
Project main file
"""
import kmedoids
import entropy
import input_reader
import numpy as np

NUMBER_OF_CLUSTER = 6
INPUT_FILE_PATH = '../data/random_1000_5.txt'

data = input_reader.read_csv_input(INPUT_FILE_PATH)

# K-Medoids algorithm
labels = kmedoids.calculate(data, NUMBER_OF_CLUSTER)
total_entropy = entropy.calculate_entropy_simple(data, labels)
print('total kmedoids entropy: ', total_entropy)

# Random
labels = np.random.randint(0, NUMBER_OF_CLUSTER, data.shape[0])
total_entropy = entropy.calculate_entropy_simple(data, labels)
print('total random entropy: ', total_entropy)