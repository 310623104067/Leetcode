class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        from collections import Counter

        cnt = Counter()
        for w in words:
            mask = 0
            for c in set(w):
                mask |= 1 << (ord(c) - 97)
            if bin(mask).count("1") <= 7:
                cnt[mask] += 1

        res = []
        for p in puzzles:
            first = 1 << (ord(p[0]) - 97)
            mask = 0
            for c in p:
                mask |= 1 << (ord(c) - 97)

            sub = mask
            total = 0
            while sub:
                if sub & first:
                    total += cnt.get(sub, 0)
                sub = (sub - 1) & mask

            res.append(total)

        return res
