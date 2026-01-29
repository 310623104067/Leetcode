class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        freq={}
        ans=0
        for d in dominoes:
            a,b=d[0],d[1]
            if a>b:
                a,b=b,a
            key=(a,b)
            ans+=freq.get(key,0)
            freq[key]=freq.get(key,0)+1
        return ans