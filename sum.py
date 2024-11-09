#two sum_leetcode
class Solution(object):
    def twoSum(self, nums, target):
        returnSize = 2  # Since we are returning exactly two indices
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
               # Check if the sum of the two numbers is equal to the target
               if nums[i] + nums[j] == target:
                   return [i, j]  
        return []  
