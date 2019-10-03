import plot_gtex
import unittest
import random
import os
from os import path


class TestPlotGtex(unittest.TestCase):

    def test_plot_gtex_linear_search_first(self):
        L = ['foo', 'bar', 'tar']
        r = plot_gtex.linear_search('foo', L)
        self.assertEqual(r, 0)

    def test_plot_gtex_linear_search_last(self):
        L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        r = plot_gtex.linear_search('g', L)
        self.assertEqual(r, 6)

    def test_plot_gtex_linear_search_gtex_files_known_idx(self):
        # Test that linear search returns the correct index for a known location
        data_file_name='GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz'
        sample_info_file_name='GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
        # This is the seventh column, so it should return an index of 6
        group_col_name = 'SMTSD'
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
        self.assertEqual(test_idx, 6)

if __name__ == '__main__':
    unittest.main()
