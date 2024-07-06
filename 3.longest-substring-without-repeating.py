# 
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Longest Substring Without Repeating Characters
# Medium
# Topics
# Companies
# Hint
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.
# 
#  
# 
# Example 1:
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#  
# 
# Constraints:
# 
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

import time
import collections

class Solution:
# sliding window
    def lengthOfLongestSubstring(self, s) -> int:
        charSet=set()
        l=0
        res=0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(res, r-l+1)
        return res
        
# sliding window
    def lengthOfLongestSubstring2(self, s: str) -> int:
        ans=0
        count=collections.Counter()
        
        l=0
        for r, c in enumerate(s):
            count[c]+=1
            while count[c]>1:
                count[s[l]] -= 1
                l += 1
            ans=max(ans, r-l+1)
            
        return ans
        
#last seen

    def lengthOfLongestSubstring3(self, s:str) -> int:
        ans=0
        j=-1
        lastSeen={}
        
        for i, c in enumerate(s):
            j=max(j,lastSeen.get(c,-1))
            ans=max(ans, i-j)
            lastSeen[c]=i
            
        return ans      
        
#last seen
s=Solution()
st = "ddddabcdabdcabceddd"

res=s.lengthOfLongestSubstring(st)
print("string: {}, lsl: {}".format(st,res))

res=s.lengthOfLongestSubstring2(st)
print("string: {}, lsl: {}".format(st,res))


res=s.lengthOfLongestSubstring3(st)
print("string: {}, lsl: {}".format(st,res))
