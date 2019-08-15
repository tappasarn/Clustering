"""
This module is a wrapper for csv input reader
It returns data which read from csv file as NumPy Array
"""
import pandas as pd
import numpy as np
import math

# Private
def _get_features(np_data):
    np_data_1d = np_data.ravel()
    nan_removed_list = [x for x in np_data_1d if x == x]

    features = np.array(list(set(nan_removed_list)))

    # next time you can load from this text file
    np.savetxt('features.csv', [features], delimiter=',', fmt='%s', newline='')

    return features

# APIs
def transformed_data(np_data):
    features = _get_features(np_data)

    data_size = np_data.shape[0]
    transform_data = np.zeros((data_size, len(features)))

    for i in range(data_size): 
        transform_data[i, :] = np.isin(features, np_data[i, :], ).astype(int)

    result = transform_data.astype(int)

    np.savetxt('transformed_binary.txt', result, delimiter=',')

    return (result, features)