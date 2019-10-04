# parallel-arrays-profiling-and-benchmarking-sahu0957
This program generates a gene expression boxplot(s) from input data

## Installation
This program should be run in a conda environment. Install conda and its dependencies as follows:
```sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
~/miniconda3/etc/profile.d/conda.sh
conda update --yes conda
conda config --add channels r
conda create --yes -n test
conda activate test
conda install -y pycodestyle
conda install --yes python=3.6
conda install matplotlib
conda install conda install -c conda-forge time
```

## Running the Program
specify input files and parameters for plot_gtex.py. This will require a gene counts file, a metadata file, a gene of interest, a metadata column of interest, where to store output, and the desired search method to use (linear or binary)
```sh
python plot_gtex.py --gene_reads /path/to/reads/data --sample_attributes /path/to/metadata --gene "Gene of interest" --group_type "Metadata of interest" --output_file /path/to/output --search_type (linear, binary)
```
## Benchmarking
Benchmarking results can be found in the following files:

```sh
less plot_gtex.binary_search.txt
less plot_gtex.linear_search.txt
less benchmarking.txt
```
The first two files show profiling results of the entire script plot_gtex.py, while the last file is a benchmarking result comparing the linear and binary search algorithms. Binary searches are much quicker, although 52% of the time is spent sorting the file before searching. As such, it is recommended that users use the binary search module.

## Testing the Program
The files test_data_viz.py, test_plot_gtex.py, test_plot_gtex.sh are test files to make sure the scripts are running properly, and will perform a suite of unit and functional tests on the scripts
```sh
python test_data_viz.py
python test_plot_gtex.py
bash test_plot_gtex.sh
```

Note that all of these tests are run in the .travis.yml CI before updating this repository on GitHub

## Release History
*1.0\
	*CHANGE: Updated data_viz.py to accept a list of lists as input, as well as x-axis, y-axis, and title information\
	*CHANGE: Updated plot_gtex.py to search through gene data and metadata, and output a boxplot using data_viz library\
	*CHANGE: Benchmarking and profiling data were generated, comparing linear and binary search algorithms\
	*CHANGE: Updated .travis.yml file to automatically perform functional/unit testing before updating GitHub repository\
    	*ADDED: Functional and unit testing scripts to ensure that all scripts are working properly\

## To Contribute
1. Fork it (< https://github.com/cu-swe4s-fall-2019/parallel-arrays-profiling-and-benchmarking-sahu0957.git>)
2. Create your feature branch (`git checkout -b feature_branch`)
3. Commit your changes (`git commit -m 'add your notes'`)
4. Push to the branch (`git push origin feature_branch`)
5. Create a new Pull request
