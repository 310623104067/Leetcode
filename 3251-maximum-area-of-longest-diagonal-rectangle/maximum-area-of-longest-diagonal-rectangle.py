class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        best_diag = 0
        best_area = 0

        for l, w in dimensions:
            d = l * l + w * w
            a = l * w
            if d > best_diag or (d == best_diag and a > best_area):
                best_diag = d
                best_area = a

        return best_area
