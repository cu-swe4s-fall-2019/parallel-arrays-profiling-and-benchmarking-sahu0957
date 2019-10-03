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

if __name__ == '__main__':
    unittest.main()
