import unittest
import math_lib
import random
import statistics
import math


class TestMathLib(unittest.TestCase):

    # These will test the robustness of the script math_lib
    # through testing empty inputs, nonnumber entries,
    # random data frames, and constant data frames with
    # known means and standard deviations
    def test_list_mean_empty_list(self):
        r = math_lib.list_mean([])
        self.assertEqual(r, None)

    def test_list_mean_constant(self):
        r = math_lib.list_mean([1, 1, 1, 1])
        self.assertEqual(r, 1)

    def test_list_mean_rand_integers(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(random.randint(0, 100))

        r = math_lib.list_mean(L)
        e = statistics.mean(L)
        self.assertEqual(r, e)

    def test_list_mean_rand_floats(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(random.random())

        r = math_lib.list_mean(L)
        e = statistics.mean(L)
        self.assertTrue(math.isclose(r, e))

    def test_list_mean_string_in_list(self):
        L = []
        for i in range(100):
            L.append(random.randint(1, 100))
        L.append('string')
        self.assertEqual(math_lib.list_mean(L),
                         'Detected nonnumber value in list! Exiting...')

    def test_list_stdev_empty_list(self):
        r = math_lib.list_stdev([])
        self.assertEqual(r, None)

    def test_list_stdev_constant(self):
        r = math_lib.list_stdev([2, 2, 2, 2])
        self.assertEqual(r, 0)

    def test_list_stdev_variable(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(random.randint(1, 100))
        r = math_lib.list_stdev(L)
        self.assertTrue(math.isclose(statistics.stdev(L), r))

    def test_list_stdev_float(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(random.random())
        r = math_lib.list_stdev(L)
        self.assertTrue(math.isclose(statistics.stdev(L), r))

    def test_list_stdev_string_in_list(self):
        L = []
        for i in range(100):
            L.append(random.randint(1, 100))
        L.append('string')
        self.assertEqual(math_lib.list_stdev(L),
                         'Detected nonnumber value in list! Exiting...')

    def test_list_stdev_one_entry(self):
        L = [1]
        self.assertEqual(math_lib.list_stdev(L), 'Cant calculate stdev on \
                         single entry! Exiting...')


if __name__ == '__main__':
    unittest.main()
