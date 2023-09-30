class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        
        sict={}
        for i in strs:
            sumss=0
            srtstr=tuple(sorted(i))
            if srtstr  not in sict:
                sict[srtstr]=[i]
            else:
                sict[srtstr].append(i)
        
        
                                        
        
        return sict.values()