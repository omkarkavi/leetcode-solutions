class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        my_map = {1:'I', 
                  5:'V',4:'IV', 10:'X',9:'IX', 50:'L', 40:'XL',100:'C',90:'XC' ,500:'D',400:'CD' ,1000:'M', 900:'CM'}
        r = ''
        mm = sorted(my_map.keys())
        #myy=sorted(mm)      
         
        for n in mm[-1::-1]:
            while n <= num:
                r = r + my_map[n]
                num = num -n
        return r