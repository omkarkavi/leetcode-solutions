class MyHashMap(object):
    my_map=[]
    def __init__(self):
        
        
        #self.my_map = [-1 for i in range(1000001)]
        self.my_map = [-1]*1000001
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.my_map[key] = value        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.my_map[key]
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.my_map[key] = -1