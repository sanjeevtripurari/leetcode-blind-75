#https://leetcode.com/problems/longest-palindromic-substring/description/
#5. Longest Palindromic Substring
#Medium
#Topics
#Companies
#Hint
#Given a string s, return the longest
#palindromic
#
#substring
# in s.
#
#
#
#Example 1:
#
#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.
#Example 2:
#
#Input: s = "cbbd"
#Output: "bb"
#
#
#Constraints:
#
#1 <= s.length <= 1000
#s consist of only digits and English letters.
#

class Solution:
    def longestPalindrome(self, s: str)->str:
        res=""
        resLen=0

        for i in range(len(s)):
            #odd length
            l,r=i,i

            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l -= 1
                r += 1

            #even length
            l,r=i,i+1

            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l -= 1
                r += 1

        return res

    def longestPalindrome_manacher(self, s: str)->str:
        t = '#'.join('@'+s+'$')
        n = len(t)
        maxExtends = [0]*n
        center = 0

        for i in range(1, n-1):
            rightBoundary = center + maxExtends[center]
            mirrorIndex = center - (i - center)
            maxExtends[i]=rightBoundary>i and min(rightBoundary - i, maxExtends[mirrorIndex])

            while t[i + 1 + maxExtends[i]] == t[i - 1 - maxExtends[i]]:
                maxExtends[i] += 1

            if i + maxExtends[i] > rightBoundary:
                center = i

        maxExtend, bestCenter = max((extend, i) for i, extend in enumerate(maxExtends))

        return s[(bestCenter - maxExtend) // 2:(bestCenter + maxExtend) // 2]



sp=Solution()
st = "rabbaopbabiopbarp"
lp = sp.longestPalindrome(st)
print("Word: {} Palindrome: {}".format(st,lp))
lp = sp.longestPalindrome_manacher(st)
print("Word: {} Palindrome: {}".format(st,lp))

 
