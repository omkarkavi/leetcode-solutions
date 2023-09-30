from collections import Counter

class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        #x = Counter(word)):
        for i in range(len(word)):
            if len(set(Counter(word[:i]+word[i+1:]).values()))==1:
                return True
        return False