"""
This module is a wrapper for csv input reader
It returns data which read from csv file as NumPy Array
"""
import pandas as pd
import numpy as np

def read_csv_input(file_name):
    # Read data from file
    df = pd.read_csv(file_name, sep=',',header=None)

    # encode all input types to interger so that it is in a generic form
    # for distance calculation
    return encode_string_input_to_integer(df.values)

def encode_string_input_to_integer(input_arr):
    num_data, num_features = input_arr.shape
    num_categories = []
    transformed_data = np.zeros((num_data, num_features))
    for i in range(num_categories):
        one_column = input_arr[:,i]
        uq_values = np.unique(one_column) 
        num_categories[i] = len(uq_values)
        temp = []
        for j in range(uq_values):
            idx = np.where(one_column==uq_values[j])[0]
            temp = np.array(one_column)
            temp[idx] = j
        transformed_data[:,i] = temp
    
    return transformed_data
