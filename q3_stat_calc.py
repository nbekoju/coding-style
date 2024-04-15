"""
Design a function that takes a list of numerical data and performs calculations for 
mean, median and standard deviation. Write unit tests to verify the correctness of 
the statistical calculations for various inputs, including edge cases 
like an empty list or a list with one element  (Use unittest module).
"""

import unittest


def calc_mean(nums: list):
    """
    calculate the mean
    """
    return sum(nums) / len(nums)


def calc_median(nums: list):
    """
    calculate the median
    """
    nums.sort()
    length = len(nums)
    if length % 2 == 0:
        median1 = nums[length // 2]
        median2 = nums[length // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = nums[length // 2]
    return median


def calc_std_dev(nums: list):
    """calculate the standard deviation"""
    mean = calc_mean(nums)
    length = len(nums)
    std_dev = 0
    for i, _ in enumerate(nums):
        std_dev += (nums[i] - mean) ** 2
    std_dev /= length
    std_dev = std_dev**0.5
    return std_dev


def calc_stats(nums: list):
    """calculate mean, median and standard deviation"""
    return calc_mean(nums), calc_median(nums), calc_std_dev(nums)


class TestValidateStats(unittest.TestCase):
    """
    validate the right and wrong stats
    """

    def test_right_stats(self):
        """validate the right stats"""
        right_test_case = [
            {
                "nums": [9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25],
                "mean": 16.75,
                "median": 15.5,
                "std_dev": 5.1173,
            },
            {
                "nums": [1, 2, 3, 4, 5],
                "mean": 3,
                "median": 3,
                "std_dev": 1.4142,
            },
            {
                "nums": [10, 12, 23, 23, 16, 23, 21, 16],
                "mean": 18,
                "median": 18.5,
                "std_dev": 4.8989,
            },
        ]

        for test_case in right_test_case:
            result = calc_stats(test_case["nums"])
            self.assertAlmostEqual(result[0], test_case["mean"], places=3)
            self.assertAlmostEqual(result[1], test_case["median"], places=3)
            self.assertAlmostEqual(result[2], test_case["std_dev"], places=3)

    def test_empty_list(self):
        """validate the empty data"""
        data = []
        with self.assertRaises(ZeroDivisionError):
            calc_stats(data)

    def test_single_element(self):
        """validate the single element"""
        single_element_case = [{"nums": [5], "mean": 5, "median": 5, "std_dev": 0}]
        for test_case in single_element_case:
            result = (test_case["mean"], test_case["median"], test_case["std_dev"])
            self.assertEqual(calc_stats(test_case["nums"]), result)


if __name__ == "__main__":
    unittest.main()
