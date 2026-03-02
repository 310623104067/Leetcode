class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        for i, ch in enumerate(s):
            if freq[ch] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left, right)
        
        return len(s)