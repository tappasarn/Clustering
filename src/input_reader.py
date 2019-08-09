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
    # return df.values
    return _encode_string_input_to_integer(df.values)

def _encode_string_input_to_integer(data):
    num_data, num_features = data.shape
    transformed_data = np.zeros((num_data, num_features))
    for i in range(num_features):
        single_column = data[:,i]
        uq_values_in_col = np.unique(single_column) 
        temp = np.array(single_column)
        for j in range(len(uq_values_in_col)):
            idx = np.where(single_column == uq_values_in_col[j])[0]
            temp[idx] = j
        transformed_data[:,i] = temp
    
    return transformed_data
