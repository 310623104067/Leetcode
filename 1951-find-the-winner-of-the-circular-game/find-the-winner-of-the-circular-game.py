class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  # 0-based index
        
        for i in range(2, n + 1):
            winner = (winner + k) % i
        
        return winner + 1  # convert to 1-based index