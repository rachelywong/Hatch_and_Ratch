# leetcode - two sum

class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if (nums[i] + nums[j] == target):
                    if (i != j):
                        return ([i,j])

test = Solution()

nums = [2,7,11,15]
target = 9

test.twoSum(nums, target)

trying to make it not so slow:

class Solution:
    def twoSum(self, nums, target):
        leftovers = [nums]
        print(leftovers)
        
        return leftovers


test = Solution()

nums = [2,7,11,15]
target = 9

test.twoSum(nums, target)

