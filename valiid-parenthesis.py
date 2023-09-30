class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stcck = []
        dcct = {'}':'{',']':'[',')':'('}
        for i in s:
            if i in '{([':
                stcck.append(i)
            elif i in '}])':
                if len(stcck) == 0 or dcct[i] != stcck.pop():
                    return False
                
                    
        return len(stcck) == 0