"""
Project main file
"""
import k_mediods
import entropy
import input_reader

NUMBER_OF_CLUSTER = 6
INPUT_FILE_PATH = '../data/random_1000_5.txt'

data = input_reader.read_csv_input(INPUT_FILE_PATH)
label = k_mediods.calculate(NUMBER_OF_CLUSTER, INPUT_FILE_PATH)

total_entropy = entropy.calculate_entropy_simple(data, label)

print('total entropy: ', total_entropy)