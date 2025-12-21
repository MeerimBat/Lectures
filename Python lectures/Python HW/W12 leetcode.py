class Solution:
    def majorityElement(self, nums: list[int]) -> int:
      nums.sort (nums)
      return nums [nums.length/2]

nums = [3,2,3]
