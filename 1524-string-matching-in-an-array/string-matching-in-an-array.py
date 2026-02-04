class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        words.sort(key=len)
        for  i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res

