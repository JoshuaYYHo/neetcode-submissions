class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for index, value in enumerate(nums):

            complement = target - value

            if complement in d:
                return [d[complement], index]

            d[value] = index
        