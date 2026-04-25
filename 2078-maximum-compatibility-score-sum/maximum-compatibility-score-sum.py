from itertools import permutations

class Solution:
    def maxCompatibilitySum(self, students, mentors):
        m = len(students)
        
        # Function to calculate compatibility score
        def score(s, m):
            return sum(1 for i in range(len(s)) if s[i] == m[i])
        
        max_score = 0
        
        # Try all permutations of mentors
        for perm in permutations(mentors):
            total = 0
            for i in range(m):
                total += score(students[i], perm[i])
            max_score = max(max_score, total)
        
        return max_score