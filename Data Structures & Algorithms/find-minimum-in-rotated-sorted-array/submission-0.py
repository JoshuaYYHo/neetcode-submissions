class Solution:
    def findMin(self, nums: List[int]) -> int:

        # take last 4 elements and put them in front

        # the literal base case
        l, r = 0, len(nums) - 1

        min_value = nums[0]
        while l <= r:
            l_val = nums[l]
            r_val = nums[r]
            min_of_pointers = min(l_val, r_val)

            if min_of_pointers <= min_value:
                min_value = min_of_pointers

            l += 1
            r -= 1



        return min_value

        