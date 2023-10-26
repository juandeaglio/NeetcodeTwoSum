from abc import abstractmethod, ABC
from typing import List, Protocol


class TwoSumStrategy(Protocol):
    @abstractmethod
    def find_two_sum(self, nums: list[int], target: int) -> list[int]:
        pass


class NaiveTwoSumStrategy(TwoSumStrategy, ABC):
    def find_two_sum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if self.is_target_sum(nums, target, i, j):
                    return [i, j]
        return []

    def is_target_sum(self, nums, target, i, j):
        return nums[i] + nums[j] == target



class HashTwoSumStrategy(TwoSumStrategy, ABC):
    def find_two_sum(self, nums: list[int], target: int) -> list[int]:
        hash_table = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table:
                return [hash_table[complement], i]
            else:
                hash_table[nums[i]] = i

class Solution:
    def __init__(self, strategy: TwoSumStrategy = None):
        self.strategy = strategy

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) > 100000:
            self.strategy = HashTwoSumStrategy()
        else:
            self.strategy = NaiveTwoSumStrategy()

        return self.strategy.find_two_sum(nums, target)
