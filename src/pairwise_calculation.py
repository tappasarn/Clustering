"""
This module is use for pairwise distance calculation
"""
import numpy as np
import math
from sklearn.metrics.pairwise import pairwise_distances

def _calculate_pairwise(X, operation):        
    
    data_size = X.shape[0]
    # Initialise precomputed matrix
    precomputed = np.zeros((data_size, data_size))
    
    for i in range(data_size):
        for j in range(i+1, data_size):
            precomputed[i,j] = operation(X[i], X[j])
            precomputed[j,i] = operation(X[i], X[j])
    
    # Make symmetric and return
    return precomputed

def _jaccard(x, y):
    number_of_intersec = _get_number_of_intersec_data(x, y)
    return 1 - number_of_intersec / (len(x)+len(y)-number_of_intersec)

def _cosine(x, y):
    number_of_intersec = _get_number_of_intersec_data(x, y)
    return 1 - number_of_intersec / math.sqrt(len(x)*len(y))

def _matching(x, y):
    number_of_intersec = _get_number_of_intersec_data(x, y)
    return 1 - number_of_intersec / max(len(x),len(y))

def _overlap(x, y):
    number_of_intersec = _get_number_of_intersec_data(x, y)
    return 1 - number_of_intersec / min(len(x),len(y))

def _get_number_of_intersec_data(x, y):
    uq1 = set(x)
    uq1.discard('')

    uq2 = set(y)
    uq2.discard('')

    return len(uq1 & uq2)

def calculate_custom(data, similarity_measure):
    if similarity_measure == 'Jaccard':
        return _calculate_pairwise(data, _jaccard)
    elif similarity_measure == 'Cosine':
        return _calculate_pairwise(data, _cosine)
    elif similarity_measure == 'Matching':
        return _calculate_pairwise(data, _matching)
    elif similarity_measure == 'Overlap':
        return _calculate_pairwise(data, _matching)
    else: 
        data_size = data.shape[0]
        return np.full((data_size, data_size), np.inf)

def calculate(input):
    return pairwise_distances(input, metric='hamming')