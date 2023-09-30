import collections
class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        c = Counter(list(s))
        i = c[letter]
        return int(i/float(len(s))*100)