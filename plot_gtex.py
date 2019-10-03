import data_viz
import argparse
import sys
import gzip

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
    parser.add_argument("--search_type", help="search type", default="linear", type=str)

    args = parser.parse_args()
    # Test that linear search returns the correct index for a known location
    data_file_name = args.gene_reads
    sample_info_file_name = args.sample_attributes
    # This is the seventh column, so it should return an index of 6
    group_col_name = args.group_type
    gene_name = args.gene
    sample_id_col_name = 'SAMPID'
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
    group_col_idx = linear_search(group_col_name, sample_info_header)
    sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)
    groups = []
    members = []

    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]
        curr_group_idx = linear_search(curr_group, groups)

        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])

        members[curr_group_idx].append(sample_name)
    version = None
    dim = None
    data_header = None

    gene_name_col = 1
    print(groups)
    group_counts = [ [] for i in range(len(groups)) ]
    for l in gzip.open(data_file_name, 'rt'):
        if version == None:
            version = l
            continue

        if dim == None:
            dim = [int(x) for x in l.strip().split()]
            continue

        if data_header == None:
            data_header = []
            i = 0
            for field in l.rstrip().split('\t'):
                data_header.append([field, i])
                i += 1
            # Sort in preparation for binary search
            if args.search_type == "binary":
                data_header.sort(key=lambda tup: tup[0])

            continue

        A = l.rstrip().split('\t')
        print(members) 
        if A[gene_name_col] == gene_name:
            for group_idx in range(len(groups)):
                for member in members[group_idx]:
                    members_idx = linear_search(member, data_header)
                    if members_idx != -1:
                        group_counts[group_idx].append(int(A[member_idx]))
            break

    print(group_counts)
    data_viz.boxplot(group_counts, 'boxplot.png')

if __name__ == '__main__':
    main()
