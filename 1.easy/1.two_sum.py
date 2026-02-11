class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        # O(n)
        nums_needed = {target - nums[i]: i for i in range(n)}
        for i in range(n):
            if nums[i] in nums_needed and i != nums_needed[nums[i]]:
                return i, nums_needed[nums[i]]
