import unittest

from main import Solution, NaiveTwoSumStrategy, HashTwoSumStrategy


class Test_TwoSum(unittest.TestCase):
    def test_two_sum_from_three_elements(self):
        naive_solution = Solution(NaiveTwoSumStrategy()).twoSum([3, 2, 1, 4], 7)
        self.assertEqual([0, 3], naive_solution)

    def test_two_sum_non_naive(self):
        naive_solution = Solution(NaiveTwoSumStrategy()).twoSum([3, 2, 1, 4], 7)
        non_naive = Solution(HashTwoSumStrategy()).twoSum([3, 2, 1, 4], 7)
        self.assertEqual(naive_solution, non_naive)

if __name__ == '__main__':
    unittest.main()
