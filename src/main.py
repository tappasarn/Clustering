"""
Project main file
"""
import clustering
import input_reader

# parameters
NUMBER_OF_CLUSTER = 4
CLUSTEING_METHOD = 'KMEDOIDS'
INPUT_FILE_PATH = '../data/data.txt'

data = input_reader.read_csv_input(INPUT_FILE_PATH)
data = data[1:20, :]

if CLUSTEING_METHOD == 'KMEDOIDS':
    labels, total_entropy, final_centroids, sc_avg = clustering.kmedoids(data, NUMBER_OF_CLUSTER)
    print('total kmedoids entropy: ', total_entropy)
    print('avg sihouette score is: ', sc_avg)
elif CLUSTEING_METHOD == 'RANDOM':
    labels, total_entropy, final_centroids, sc_avg = clustering.randomize(data, NUMBER_OF_CLUSTER)
    print('total random entropy: ', total_entropy)
    print('avg sihouette score is: ', sc_avg)
elif CLUSTEING_METHOD == 'KMODES':
    labels, total_entropy, final_centroids, sc_avg = clustering.kmodes(data, NUMBER_OF_CLUSTER)
    print('total kmode entropy: ', total_entropy)
    print('avg sihouette score is: ', sc_avg)
elif CLUSTEING_METHOD == 'KHISTOGRAMS':
    labels, total_entropy, final_centroids, sc_avg = clustering.khistograms(data, NUMBER_OF_CLUSTER)
    print('total khistogram entropy: ', total_entropy)  
    print('avg sihouette score is: ', sc_avg)