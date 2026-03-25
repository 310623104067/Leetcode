class Solution(object):
    def beautifulArray(self, n):
        res = [1]
        
        while len(res) < n:
            temp = []
            
            # odd part
            for x in res:
                if 2 * x - 1 <= n:
                    temp.append(2 * x - 1)
            
            # even part
            for x in res:
                if 2 * x <= n:
                    temp.append(2 * x)
            
            res = temp
        
        return res