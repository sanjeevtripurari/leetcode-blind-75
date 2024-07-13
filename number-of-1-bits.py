#https://leetcode.com/problems/number-of-1-bits/description/
#
#191. Number of 1 Bits
#Easy
#
#Topics
#Companies
#Write a function that takes the binary representation of a positive integer and returns the number of 
#set bits
# it has (also known as the Hamming weight).
#
# 
#
#Example 1:
#
#Input: n = 11
#
#Output: 3
#
#Explanation:
#
#The input binary string 1011 has a total of three set bits.
#
#Example 2:
#
#Input: n = 128
#
#Output: 1
#
#Explanation:
#
#The input binary string 10000000 has a total of one set bit.
#
#Example 3:
#
#Input: n = 2147483645
#
#Output: 30
#
#Explanation:
#
#The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
#
#

class Solution:
    def countbits(self, no:int)->int:
        c=0
        while no:
            c += (no & 1)
            no >>= 1
        return c

s=Solution()
n=11
c=s.countbits(n)
print("n: {}, b:{}, bits: {}".format(n,bin(n),c))

n=1011
c=s.countbits(n)
print("n: {}, b:{}, bits: {}".format(n,bin(n),c))

n=128
c=s.countbits(n)
print("n: {}, b:{}, bits: {}".format(n,bin(n),c))
