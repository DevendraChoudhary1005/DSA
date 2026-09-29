class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m+n-1) % 2 != 0:
            return False
        
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        
        start_state = (0, 0, 1)
        stack = [start_state]
        visited = {start_state}

        while stack:
            r, c, balance = stack.pop()

            if r == m-1 and c == n-1:
                if balance == 0:
                    return True
                continue
            
            for dr, dc in ((1, 0), (0, 1)):
                nr, nc = r+dr, c+dc

                if nr < m and nc < n:
                    new_balance = balance + (1 if grid[nr][nc] == '(' else -1)

                    if new_balance < 0:
                        continue

                    remaining_steps = (m-1-nr) + (n-1-nc)

                    if new_balance > remaining_steps:
                        continue

                    next_state = (nr, nc, new_balance)
                    if next_state not in visited:
                        visited.add(next_state)
                        stack.append(next_state)

        return False
