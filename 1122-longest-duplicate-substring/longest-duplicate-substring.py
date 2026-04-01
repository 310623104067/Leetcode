class Solution(object):
    def longestDupSubstring(self, s):
        n = len(s)
        nums = [ord(c) - ord('a') for c in s]
        base = 26
        mod = 2**63 - 1
        
        def check(L):
            h = 0
            for i in range(L):
                h = (h * base + nums[i]) % mod
            
            seen = {h}
            baseL = pow(base, L, mod)
            
            for i in range(L, n):
                h = (h * base - nums[i - L] * baseL + nums[i]) % mod
                if h in seen:
                    return i - L + 1
                seen.add(h)
            
            return -1
        
        left, right = 1, n
        start = -1
        
        while left <= right:
            mid = (left + right) // 2
            idx = check(mid)
            
            if idx != -1:
                start = idx
                left = mid + 1
            else:
                right = mid - 1
        
        return "" if start == -1 else s[start:start + left - 1]