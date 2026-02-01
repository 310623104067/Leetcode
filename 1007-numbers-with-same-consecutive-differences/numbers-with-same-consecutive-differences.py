class Solution(object):
    def numsSameConsecDiff(self, n, k):
        if n == 1:
            return [0,1,2,3,4,5,6,7,8,9]

        cur = [1,2,3,4,5,6,7,8,9]

        for _ in range(n - 1):
            nxt = []
            for num in cur:
                last = num % 10
                a = last + k
                b = last - k

                if a <= 9:
                    nxt.append(num * 10 + a)
                if k != 0 and b >= 0:
                    nxt.append(num * 10 + b)

            cur = nxt

        return cur
