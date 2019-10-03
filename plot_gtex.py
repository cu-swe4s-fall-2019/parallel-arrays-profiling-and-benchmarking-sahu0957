import data_viz
import argparse
import sys

def linear_search(key, L):
    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i
    return -1
        

def binary_serach(key, L):
    pass


def main():
    parser = argparse.ArgumentParser(
    description="plot gene expression boxplots of a gene across multiple samples")
    parser.add_argument("--gene_reads", help="path to file containing gene reads", type=str)
    parser.add_argument("--sample_attributes", help="path to file containing sample informtion", type=str)
    parser.add_argument("--gene", help="name of gene of interest", type=str)
    parser.add_argument("--group_type", help="group info to search for", default="SMTS", type=str)
    parser.add_argument("--output_file", help="path to save output PNG file", type=str)

    args = parser.parse_args()
    # Test that linear search returns the correct index for a known location
    data_file_name = args.gene_reads
    sample_info_file_name = args.sample_attributes
    # This is the seventh column, so it should return an index of 6
    group_col_name = args.group_type
    gene_name = args.gene
    samples = []
    sample_info_header = None
    for l in open(sample_info_file_name):
        # If the list is empty, then make the first line a header
        if sample_info_header == None:
            sample_info_header = l.strip().split('\t')
        else:
            # Add each line to the growing list until we've gone through
            # the whole file
            samples.append(l.rstrip().split('\t'))
        # Find the index of the group name in the info file
    test_idx = plot_gtex.linear_search(group_col_name, sample_info_header)

if __name__ == '__main__':
    main()
