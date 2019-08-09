"""
This module calculates clusters by using random algorithm
"""
import numpy as np

def calculate(data, number_of_cluster):
    return np.random.randint(0, number_of_cluster, data.shape[0])
