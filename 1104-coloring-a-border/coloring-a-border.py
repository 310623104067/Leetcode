class Solution:
    def colorBorder(self, grid, row, col, color):
        m, n = len(grid), len(grid[0])
        original = grid[row][col]
        visited = [[False] * n for _ in range(m)]
        borders = []

        def dfs(r, c):
            visited[r][c] = True
            is_border = False
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] != original:
                        is_border = True
                    elif not visited[nr][nc]:
                        dfs(nr, nc)
                else:
                    is_border = True

            if is_border:
                borders.append((r, c))

        dfs(row, col)

        for r, c in borders:
            grid[r][c] = color

        return grid
