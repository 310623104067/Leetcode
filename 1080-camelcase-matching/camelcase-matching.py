class Solution(object):
    def camelMatch(self, queries, pattern):
        def match(q, p):
            i = 0
            for ch in q:
                if i < len(p) and ch == p[i]:
                    i += 1
                elif 'A' <= ch <= 'Z':
                    return False
            return i == len(p)

        res = []
        for q in queries:
            res.append(match(q, pattern))
        return res
