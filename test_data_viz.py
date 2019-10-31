import unittest
import data_viz
import random
import os
from os import path


class TestDataViz(unittest.TestCase):

    def test_data_viz_multiple_lists_boxplot(self):
        L = [[1, 2, 3, 4, 5], [3, 3, 3, 3, 3],
             [5, 5, 5, 5, 5], [10, 20, 30, 40, 50]]
        r = data_viz.boxplot(L, [], 'test_boxplot')
        self.assertTrue(path.exists('test_boxplot.png'))

    def test_data_viz_empty_list_boxplot(self):
        # Test handling of empty lists
        L = []
        r = data_viz.boxplot(L, [], 'boxplot')
        self.assertEqual(r, None)

    def test_data_viz_constant_boxplot(self):
        # Test creation of boxplot.png
        L = [1, 2, 3, 4, 5]
        data_viz.boxplot(L, [], 'boxplot.png')
        self.assertTrue(path.exists("boxplot.png"))

    def test_data_viz_nonnumber_boxplot(self):
        # Test handling of nonnumber entries
        L = ['foo', 'bar']
        with self.assertRaises(TypeError) as ex:
            data_viz.boxplot(L, [], 'boxplot.png')

    def test_data_viz_float_boxplot(self):
        # Test handling of floats
        L = [1.0, 2.2, 5.1, 3.8, 4.9]
        data_viz.boxplot(L, [], 'boxplot.png')
        self.assertTrue(path.exists("boxplot.png"))

    def test_data_viz_empty_list_histogram(self):
        # Test handling of empty input
        L = []
        r = data_viz.histogram(L, 'histogram.png')
        self.assertEqual(r, None)

    def test_data_viz_constant_histogram(self):
        # Test that histogram.png is successfully
        # created
        L = [1, 2, 3, 4, 5]
        data_viz.histogram(L, 'histogram.png')
        self.assertTrue(path.exists("histogram.png"))

    def test_data_viz_float_histogram(self):
        # Test handling of floats
        L = [1.0, 2.2, 5.1, 3.8, 4.9]
        data_viz.histogram(L, 'histogram.png')
        self.assertTrue(path.exists("histogram.png"))

    def test_data_viz_empty_list_combo(self):
        # Test that the script returns None when
        # input list is empty
        L = []
        r = data_viz.boxplot(L, [], 'combo.png')
        self.assertEqual(r, None)

    def test_data_viz_constant_combo(self):
        # Test creation of a PNG from the script
        L = [1, 2, 3, 4, 5]
        data_viz.combo(L, 'combo.png')
        self.assertTrue(path.exists("combo.png"))

    def test_data_viz_nonnumber_combo(self):
        # Test error handling with nonnumber entries
        L = ['foo', 'bar']
        with self.assertRaises(TypeError) as ex:
            data_viz.combo(L, 'combo.png')

    def test_data_viz_float_combo(self):
        # Test script's robustness with floats
        L = [1.0, 2.2, 5.1, 3.8, 4.9]
        data_viz.combo(L, 'combo.png')
        self.assertTrue(path.exists("combo.png"))

    def tearDown(self):
        # Remove all temporary files created during
        # testing
        if path.exists("boxplot.png"):
            os.remove("boxplot.png")
        if path.exists("histogram.png"):
            os.remove("histogram.png")
        if path.exists("combo.png"):
            os.remove("combo.png")


if __name__ == '__main__':
    unittest.main()
