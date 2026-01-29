class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        base=[0]*26
        for ch in chars:
            base[ord(ch)-ord('a')]+=1
        total=0
        for w in words:
            cnt=[0]*26
            ok=True
            for ch in w:
                idx=ord(ch)-ord('a')
                cnt[idx]+=1
                if cnt[idx]>base[idx]:
                    ok=False
                    break
            if ok:
                total+=len(w)
        return total
