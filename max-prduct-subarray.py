#https://leetcode.com/problems/maximum-product-subarray/description/
#
#152. Maximum Product Subarray
#Medium
#
#Topics
#Companies
#Given an integer array nums, find a 
#subarray
# that has the largest product, and return the product.
#
#The test cases are generated so that the answer will fit in a 32-bit integer.
#
# 
#
#Example 1:
#
#Input: nums = [2,3,-2,4]
#Output: 6
#Explanation: [2,3] has the largest product 6.
#Example 2:
#
#Input: nums = [-2,0,-1]
#Output: 0
#Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#
#Constraints:
#
#1 <= nums.length <= 2 * 104
#-10 <= nums[i] <= 10
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

from typing import List

class Solution:
    def maxProductArray(self, nums: List[int]) -> int:
        res=imax=imin=nums[0]
        for num in nums[1:]:
            if num<0:
                imax, imin = imin,imax
            imax = max(imax * num, num)
            imin = min(imin * num, num)
            res  = max(res, imax)
        return res

s=Solution()

nums1 = [2,3,-2,4]
nums = nums1[:]
m=s.maxProductArray(nums)
print("nums: {}, max: {}".format(nums1,m))

nums1 = [-2,0,-1]
nums = nums1[:]
m=s.maxProductArray(nums)
print("nums: {}, max: {}".format(nums1,m))
