class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n,m=len(matrix),len(matrix[0])
        px=[[0]*(m+1) for _ in range(n+1)]
        vals=[]
        for i in range(1,n+1):
            for j in range(1,m+1):
                px[i][j]=(matrix[i-1][j-1]^px[i-1][j]^px[i][j-1]^px[i-1][j-1])
                vals.append(px[i][j])
        vals.sort(reverse=True)
        return vals[k-1]

        