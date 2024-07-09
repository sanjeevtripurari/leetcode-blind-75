## https://leetcode.com/problems/contains-duplicate/description/
## 217. Contains Duplicate
#Easy
#
#Topics
#Companies
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,3,1]
#Output: true
#Example 2:
#
#Input: nums = [1,2,3,4]
#Output: false
#Example 3:
#
#Input: nums = [1,1,1,3,3,4,3,2,4,2]
#Output: true
# 
#
#Constraints:
#
#1 <= nums.length <= 105
#-109 <= nums[i] <= 109

class Solution:
    def contains(self, nums):
        s=set()
        for n in nums:
            if n in s:
                return True
            s.add(n)

        return False

s=Solution()
a=[1,2,5,6,7]
v=s.contains(a)
print("A: {}, C: {}".format(a,v))

a=[1,2,5,6,7,5]
v=s.contains(a)
print("A: {}, C: {}".format(a,v))


