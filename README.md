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


## How to use
You just need to import `clustering` into your file. Then, you get to enjoy the APIs it provides.

### Example
```py
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
```