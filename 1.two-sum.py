##
# https://leetcode.com/problems/two-sum/description/'
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.



#Example 1:
#
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Example 2:
#
#Input: nums = [3,2,4], target = 6
#Output: [1,2]
#Example 3:la

# Input: nums = [3,3], target = 6
#Output: [0,1]



class Solution:
# Brute force
    def twoSum_bf(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """
        i=0
        while i<len(nums)-1:
            j=i+1
            while j<len(nums):
                if nums[i]+nums[j]==target:
                    return (i,j)
                j=j+1
            i=i+1


    def twoSum(self, nums, target):
        num_indices={}
        for i, n in enumerate(nums):
            diff=target-n
            if diff in num_indices:
                return (num_indices[diff],i)
            num_indices[n]=i
        

f=Solution()
nums=[2,7,11,15]
target=18

i=f.twoSum(nums,target)
 
print("nums: {}, target: {}".format(nums,target)) 
print("Indices: {}".format(i))


            
