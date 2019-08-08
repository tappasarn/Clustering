# K-Mediods

This is a source code for Python implementation of K-Mediods algorithm.

## Distance
For this module, the distance calculation will base on hamming algorithm.

## API
* Calculation : takes number of cluster (mediods) and a string for input file path

## Input
* number_of_mediods: int
* input_file_path: string

## Output
When the computation is finished. The indices of the data will be printed to a text file called `cluster_members_idx`
Each cluster as the results will be separated by `\n` (next line)

## To run
1) Create a main file
2) import `k_mediods` module
3) supply needed inputs for `calucation` api
3) run !

## TODO
1) Support multiple distance calculation algorithm
2) Optimize performance

*I try to make this code easy to read. Therefore, variable names are a bit long. Moreover, the code in here is not optimize to conserve the readability*