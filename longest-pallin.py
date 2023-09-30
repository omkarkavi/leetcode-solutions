class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
        pString=0
        result=[]
        for i in range(len(s)):
            
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>pString:
                    pString=r-l+1
                    result=s[l:r+1]


                l=l-1
                r=r+1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>pString:
                    pString=r-l+1
                    result=s[l:r+1]


                l=l-1
                r=r+1
        return result