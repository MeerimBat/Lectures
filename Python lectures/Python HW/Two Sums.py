#1
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        hash_map = dict()
        for i in range(n):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[nums[i]] = i
        #nums = [2,7,11,15], target == 9

#2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]