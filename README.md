# Clustering

This library contains a set of clustering algorithms implemented in Python.
The intention of this library is to make the code very easy to read and maintain.
Therefore, variable names are a bit long and there are some optimization tradeoff.

## APIs
1) kmedoids
    * Arguments:
        * n-dimention numpy array
        * number_of_mediods
    * *Returns:* a tuple of following
        * labels: 1-dimention array contains index of clustes that each element reside in
        * total entropy: the number of entropy amount
        * final medoids: 1-dimention array contain index of final mediods that create the final cluster

2) randomize
    * *Arguments:*
        * n-dimention numpy array
        * number_of_mediods
    * *Returns:* a tuple of following
        * labels: 1-dimention array contains index of clustes that each element reside in
        * total entropy: the number of entropy amount
        * None
3) kmodes
    * *Arguments:*
        * n-dimention numpy array
        * number_of_mediods
    * *Returns:* a tuple of following
        * labels: 1-dimention array contains index of clustes that each element reside in
        * total entropy: the number of entropy amount
        * final mode: 2-dimention array with size of number_of_modes * feature_size containing the final modes
4) khistogram
    * *Arguments:*
        * n-dimention numpy array
        * number_of_mediods
    * *Returns:* a tuple of following
        * labels: 1-dimention array contains index of clustes that each element reside in
        * total entropy: the number of entropy amount
        * final histogram: a list that contains numpy arrays (final histograms) 

## How to use
You just need to import `clustering` into your file. Then, you get to enjoy the APIs it provides.

### Example
```py
"""
Project main file
"""
import clustering
import input_reader

# parameters
NUMBER_OF_CLUSTER = 6
CLUSTEING_METHOD = 'RANDOM'
INPUT_FILE_PATH = '../data/random_1000_5.txt'

data = input_reader.read_csv_input(INPUT_FILE_PATH)

if CLUSTEING_METHOD == 'KMEDOIDS':
    labels, total_entropy, final_centroids = clustering.kmedoids(data, NUMBER_OF_CLUSTER)
    print('total kmedoids entropy: ', total_entropy)
elif CLUSTEING_METHOD == 'RANDOM':
    labels, total_entropy, final_centroids = clustering.randomize(data, NUMBER_OF_CLUSTER)
    print('total random entropy: ', total_entropy)
elif CLUSTEING_METHOD == 'KMODES':
    labels, total_entropy, final_centroids = clustering.kmodes(data, NUMBER_OF_CLUSTER)
    print('total kmode entropy: ', total_entropy)
elif CLUSTEING_METHOD == 'KHISTOGRAMS':
    labels, total_entropy, final_centroids = clustering.khistogram(data, NUMBER_OF_CLUSTER)
    print('total khistogram entropy: ', total_entropy)  
```