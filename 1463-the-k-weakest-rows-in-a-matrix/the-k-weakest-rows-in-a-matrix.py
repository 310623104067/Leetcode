class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        st=[]
        for i,row in enumerate(mat):
            st.append((sum(row),i))
        st.sort()
        return[idx for _,idx in st[:k]]

        