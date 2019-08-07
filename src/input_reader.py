"""
This module is a wrapper for csv input reader
It returns data which read from csv file as NumPy Array
"""
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def read_csv_input(file_name):
    # Read data from file
    df = pd.read_csv(file_name, sep=',',header=None)

    # Our data is not number we should transform it to integer
    # so we can test the output with other modules on the internet
    return encode_string_input_to_integer(df.values)

    # return df.values

def encode_string_input_to_integer(input_arr):
    enc = OneHotEncoder(handle_unknown='ignore')
    transformed_data = enc.fit_transform(input_arr).toarray()
    return transformed_data
