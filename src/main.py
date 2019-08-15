"""
Project main file
"""
import clustering
import input_reader

# parameters
NUMBER_OF_CLUSTER = 6
CLUSTEING_METHOD = 'KHISTOGRAMS'
INPUT_FILE_PATH = '../data/random_1000_5.txt'

data = input_reader.read_csv_input(INPUT_FILE_PATH)

if CLUSTEING_METHOD == 'KMEDOIDS':
    labels, final_centroids = clustering.kmedoids(data, NUMBER_OF_CLUSTER)
elif CLUSTEING_METHOD == 'RANDOM':
    labels, final_centroids = clustering.randomize(data, NUMBER_OF_CLUSTER)
elif CLUSTEING_METHOD == 'KMODES':
    labels, final_centroids = clustering.kmodes(data, NUMBER_OF_CLUSTER)
elif CLUSTEING_METHOD == 'KHISTOGRAMS':
    labels, final_centroids = clustering.khistograms(data, NUMBER_OF_CLUSTER)