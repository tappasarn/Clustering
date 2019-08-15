"""
This module is use for pairwise distance calculation
"""
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances

def calculate(input):
    return pairwise_distances(input, metric='jaccard')
