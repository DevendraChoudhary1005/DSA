from heapq import heappop, heappush
from math import inf

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        # Build the adjacency list
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            
        # dist[u][cur] stores the minimum distance to reach node u with a streak of 'cur'
        dist = [[inf] * (k + 1) for _ in range(n)]
        
        # Start at node 0 with an initial streak length of 1 (containing labels[0])
        dist[0][1] = 0
        pq = [(0, 0, 1)]  # (distance, node, current_streak)
        
        while pq:
            d, u, cur = heappop(pq)
            
            # If we reached the destination node, return the distance
            if u == n - 1:
                return d
                
            # Skip if we've already found a shorter path to this state
            if d > dist[u][cur]:
                continue
                
            for v, w in g[u]:
                # Calculate the next streak length
                nxt = 1 if labels[v] != labels[u] else cur + 1
                nd = d + w
                
                # Check constraints and relaxation condition
                if nxt <= k and nd < dist[v][nxt]:
                    dist[v][nxt] = nd
                    heappush(pq, (nd, v, nxt))
                    
        return -1   