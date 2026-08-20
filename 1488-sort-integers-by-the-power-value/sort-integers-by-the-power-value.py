class Solution:
    def getKth(self, lo, hi, k):
        def power(x):
            count = 0

            while x != 1:
                if x % 2 == 0:
                    x //= 2
                else:
                    x = 3 * x + 1

                count += 1

            return count

        arr = []

        for x in range(lo, hi + 1):
            arr.append((power(x), x))

        arr.sort()

        return arr[k - 1][1]