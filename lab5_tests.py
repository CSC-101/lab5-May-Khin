import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add_1(self):
        # Test 1: Simple addition without overflow
        time1 = data.Time(1, 30, 45)
        time2 = data.Time(2, 20, 15)
        result = lab5.time_add(time1, time2)
        expected = data.Time(3, 51, 0)
        self.assertEqual((result.hour, result.minute, result.second),
                         (expected.hour, expected.minute, expected.second))


    def test_time_add_2(self):
        # Test 1: Simple addition without overflow
        time1 = data.Time(4, 23, 12)
        time2 = data.Time(2, 20, 15)
        result = lab5.time_add(time1, time2)
        expected = data.Time(6, 43, 27)
        self.assertEqual((result.hour, result.minute, result.second),
                         (expected.hour, expected.minute, expected.second))


    # Part 4
    def test_is_descending_1(self):
        input = [5.0, 3.0, 1.0]
        result = lab5.is_descending(input)
        expected = True
        self.assertEqual(expected, result)

    def test_is_descending_2(self):
        input = [4.7, 3.2, 5.1]
        result = lab5.is_descending(input)
        expected = False
        self.assertEqual(expected, result)


    # Part 5
    def test_larger_between_1(self):
        input = [1, 3, 2, 5, 4]
        result = lab5.large_between(input, 1, 3)
        expected = 3  # Index of 5
        self.assertEqual(expected, result)

    def test_larger_between_2(self):
        input = [10, 20, 5, 30, 25]
        result = lab5.large_between(input, 0, 4)
        expected = 3  # Index of 30
        self.assertEqual(expected, result)


    # Part 6
    def test_furthest_from_origin(self):
        points = [data.Point(1, 1), data.Point(2, 2), data.Point(3, 4)]
        result = lab5.furthest_from_origin(points)
        expected = 2
        self.assertEqual(result, expected)




if __name__ == '__main__':
    unittest.main()
