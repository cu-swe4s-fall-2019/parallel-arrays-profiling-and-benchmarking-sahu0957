import data_viz
import time
import argparse
import sys
import gzip
import os
from os import path


def linear_search(key, L):
    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i
    return -1


def binary_search(key, D):
    lo = -1
    hi = len(D)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == D[mid][0]:
            return D[mid][1]

        if (key < D[mid][0]):
            hi = mid
        else:
            lo = mid

    return -1


def main():
    parser = argparse.ArgumentParser(
            description="plot gene expression boxplots of a\
            gene across multiple samples")
    parser.add_argument("--gene_reads",
                        help="path to file containing gene reads", type=str)
    parser.add_argument("--sample_attributes",
                        help="path to file containing sample informtion",
                        type=str)
    parser.add_argument("--gene", help="name of gene of interest", type=str)
    parser.add_argument("--group_type",
                        help="group info to search for",
                        default="SMTS",
                        type=str)
    parser.add_argument("--output_file",
                        help="path to save output PNG file",
                        type=str)
    parser.add_argument("--search_type",
                        help="search type",
                        default="linear",
                        type=str)

    args = parser.parse_args()
    # Check to make sure proper search function is specified
    if (args.search_type == 'linear' or args.search_type == 'binary'):
        pass
    else:
        print('search parameter not recognized! Exiting...')
        sys.exit(1)

    # Check to make sure all paths exist
    if path.exists(args.gene_reads):
        data_file_name = args.gene_reads
    else:
        print("gene file does not exist! exiting...")
        sys.exit(1)
    if path.exists(args.sample_attributes):
        sample_info_file_name = args.sample_attributes
    else:
        print("attributes file does not exist! exiting...")
        sys.exit(1)

    group_col_name = args.group_type
    gene_name = args.gene
    sample_id_col_name = 'SAMPID'
    samples = []
    sample_info_header = None
    for l in open(sample_info_file_name):
        # If the list is empty, then make the first line a header
        if sample_info_header is None:
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
        # Only add to groups if the current index isn't found in our growing
        # groups list
        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])
        # Parallel array linking samples (members) to their tissue type (group)
        members[curr_group_idx].append(sample_name)

    version = None
    dim = None
    data_header = None
    gene_name_col = 1
    group_counts = [[] for i in range(len(groups))]
    # Open read data, categorize first two rows as
    # version and dimension rows
    for l in gzip.open(data_file_name, 'rt'):
        if version is None:
            version = l
            continue

        if dim is None:
            dim = [int(x) for x in l.strip().split()]
            continue

        if data_header is None:
            data_header = []
            i = 0
            if args.search_type == 'linear':
                data_header = l.rstrip().split('\t')
            elif args.search_type == 'binary':
                # binary search requires including tuples for sorting
                t0_sort = time.time()
                for field in l.rstrip().split('\t'):
                    data_header.append([field, i])
                    i += 1
            # Sort in preparation for binary search
            # and time for benchmarking
                data_header.sort(key=lambda tup: tup[0])
                t1_sort = time.time()

        # Parallel array containing read counts for each sample
        A = l.rstrip().split('\t')
        if A[gene_name_col] == gene_name:
            t0_search = time.time()
            for group_idx in range(len(groups)):
                for member in members[group_idx]:
                    if args.search_type == 'linear':
                        members_idx = linear_search(member, data_header)
                    else:
                        members_idx = binary_search(member, data_header)
                    if members_idx != -1:
                        group_counts[group_idx].append(int(A[members_idx]))
            t1_search = time.time()
            break

    data_viz.boxplot(group_counts, 'boxplot.png')
    # Benchmarking information
    if args.search_type == 'linear':
        total_time = t1_search - t0_search
        print("linear search time:", total_time)
    elif args.search_type == 'binary':
        total_time = t1_search - t0_sort
        print("binary search time:",
              total_time,
              (t1_sort-t0_sort)/(total_time),
              (t1_search-t0_search)/(total_time))


if __name__ == '__main__':
    main()
