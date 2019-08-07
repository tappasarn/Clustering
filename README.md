# K-Mediods

This is a source code for Python implementation of K-Mediods algorithm.

## Distance
For this module, the distance calculation will base on hamming algorithm.

## Output
When the computation is finished. The indices of the data will be printed to a text file called `cluster_members_idx`
Each cluster as the results will be separated by `\n` (next line)

## To run
1) Create `data` folder and put your data into it
2) In file `k_mediods.py` add file name into `input_arr = input_reader.read_csv_input('')`
3) run

*I try to make this code easy to read. Therefore, variable names are a bit long. Moreover, the code in here is not optimize to conserve the readability*