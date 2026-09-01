from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litters = {}
        count = 0
        start = None
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litters[(r, c)] = count
                    count += 1
                    
        if count == 0:
            return 0
            
        queue = deque([(start[0], start[1], energy, 0, 0)])
        
        max_energy_seen = {(start[0], start[1], 0): energy}
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, cur_e, mask, steps = queue.popleft()
            
            if max_energy_seen.get((r, c, mask), -1) > cur_e:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    if classroom[nr][nc] == 'X':
                        continue
                        
                    next_e = cur_e - 1
                    
                    if next_e < 0:
                        continue
                        
                    if classroom[nr][nc] == 'R':
                        next_e = energy
                        
                    next_mask = mask
                    if (nr, nc) in litters:
                        next_mask |= (1 << litters[(nr, nc)])
                        
                    if next_mask == (1 << count) - 1:
                        return steps + 1

                    if next_e > max_energy_seen.get((nr, nc, next_mask), -1):
                        max_energy_seen[(nr, nc, next_mask)] = next_e
                        queue.append((nr, nc, next_e, next_mask, steps + 1))

        return -1