import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p, q)
        
        m = p // g
        n = q // g
        
        if m % 2 == 1 and n % 2 == 1:
            return 1
        if m % 2 == 1 and n % 2 == 0:
            return 0
        if m % 2 == 0 and n % 2 == 1:
            return 2