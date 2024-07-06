##
# https://leetcode.com/problems/sum-of-two-integers/description/
# 371. Sum of Two Integers
# Medium
# Topics
# Companies
# Given two integers a and b, return the sum of the two integers without using the operators + and -.
# 
#   
#  
# Example 1:
# 
# Input: a = 1, b = 2
# Output: 3
# Example 2:
# 
# Input: a = 2, b = 3
# Output: 5
#  
# 
# Constraints:

class Solution:
	def sum2num(self, a, b):
		while(b!=0):
			carry=(a&b)
			a=a^b
			b=carry<<1
		return a
		
a=14
b=12
f=Solution()
s=f.sum2num(a,b)
print("Sum: {}+{} = {}".format(a,b,s))
