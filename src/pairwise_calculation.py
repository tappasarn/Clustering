"""
This module is use for pairwise distance calculation
"""
import numpy as np
import math
from sklearn.metrics.pairwise import pairwise_distances

def _calculate_pairwise(X, operation, log):        
    
    data_size = X.shape[0]
    # Initialise precomputed matrix
    precomputed = np.zeros((data_size, data_size))
    
    for i in range(data_size):
        for j in range(i+1, data_size):
            precomputed[i,j] = operation(X[i], X[j],log)
            precomputed[j,i] = operation(X[i], X[j],log)
    
    # Make symmetric and return
    return precomputed

def _jaccard(x, y, log):
    if log == 0:
        number_of_intersec = _get_number_of_intersec_data(x, y)
        return 1 - (number_of_intersec / _get_number_of_union_data(x, y, log))
    else: 
        number_of_intersec = len(np.bitwise_and(np.array(x).astype(bool), np.array(y).astype(bool)))
        number_of_union = len(np.bitwise_or(np.array(x).astype(bool), np.array(y).astype(bool)))
        return 1 - (number_of_intersec / number_of_union)

def _cosine(x, y, log):
    number_of_intersec = _get_number_of_intersec_data(x, y)
    return 1 - number_of_intersec / math.sqrt(len(x)*len(y))

def _matching(x, y, log):
    number_of_intersec = _get_number_of_intersec_data(x, y)
    return 1 - number_of_intersec / max(len(x),len(y))

def _overlap(x, y, log):
    number_of_intersec = _get_number_of_intersec_data(x, y)
    return 1 - number_of_intersec / min(len(x),len(y))

def _shared_idx(x, y, log):
    intersec = x & y
    return len(np.where(intersec == 1)[0])

def _get_number_of_intersec_data(x, y):
    uq1 = set(x)
    uq1.discard('')

    uq2 = set(y)
    uq2.discard('')

    return len(uq1 & uq2)

def _get_number_of_union_data(x, y, log):
    uq1 = set(x)
    uq1.discard('')

    uq2 = set(y)
    uq2.discard('')

    return len(uq1 | uq2)

def calculate_custom(data, similarity_measure, log=0):
    if similarity_measure == 'Jaccard':
        return _calculate_pairwise(data, _jaccard, log)
    elif similarity_measure == 'Cosine':
        return _calculate_pairwise(data, _cosine, 0)
    elif similarity_measure == 'Matching':
        return _calculate_pairwise(data, _matching, 0)
    elif similarity_measure == 'Overlap':
        return _calculate_pairwise(data, _overlap, 0)
    elif similarity_measure == 'SharedIndex':
        return _calculate_pairwise(data, _shared_idx, 0)
    else: 
        data_size = data.shape[0]
        return np.full((data_size, data_size), np.inf)

def calculate(input):
    return pairwise_distances(input, metric='jaccard')