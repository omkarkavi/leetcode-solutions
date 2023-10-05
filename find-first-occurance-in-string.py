class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if haystack == needle:
            return 0
        
        nl = len(needle)
        
        for i in range(len(haystack)-nl+1):
            if haystack[i:i+nl] == needle:
                return i
        return -1