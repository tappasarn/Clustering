"""
This module is a wrapper for csv input reader
It returns data which read from csv file as NumPy Array
"""
import numpy as np
from itertools import chain

# Private
def _get_features(np_data):
    # np_data_1d = np_data.ravel()
    np_data_1d = list(chain.from_iterable(np_data))
    # nan_removed_list = [x for x in np_data_1d if x == x]

    features = np.array(list(set(np_data_1d)))

    # next time you can load from this text file
    np.savetxt('features.csv', [features], delimiter=',', fmt='%s', newline='')

    return features

# APIs
def transformed_data(np_data):
    features = _get_features(np_data)

    data_size = np_data.shape[0]
    transform_data = np.zeros((data_size, len(features)))
    
    for i in range(data_size): 
        transform_data[i, :] = np.isin(features, np_data[i]).astype(int)
        
    return transform_data.astype(int)
    