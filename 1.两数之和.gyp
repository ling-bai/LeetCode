 #coding=utf-8

# https://leetcode-cn.com/problems/two-sum/

# 题目：
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
#  所以返回 [0, 1]

# 思路：
# 使用散列表，缓存访问过的元素和下标，遍历数组，查找缓存中是否存在元素和当前元素的和等于目标值。 时间复杂度 O(n)。 

# 答案：
# O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numberIndexDict = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in numberIndexDict:
                return [numberIndexDict[y], i]
            # 存下标
            numberIndexDict[x] = i