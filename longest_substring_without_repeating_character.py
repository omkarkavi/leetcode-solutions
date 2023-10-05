class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<2:
            return len(s)
        if len(s)==2:
            if s[0]==s[1]:
                return 1
            else:
                return 2
        charSet=set()
        maxLen=0
        l,r=0,0
        
        while r<len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l=l+1
            
            charSet.add(s[r])
            r=r+1
            maxLen=max(maxLen,r-l)
        return maxLen    