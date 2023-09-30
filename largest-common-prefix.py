class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shr,lon = min(strs), max(strs)
        res = ''
        for i in range(len(shr)):
            if shr[i] == lon[i]:
                res = res + shr[i]
            else:
                return res
        return res
            