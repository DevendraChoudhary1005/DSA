from collections import defaultdict, deque
from typing import List


class Solution:

  def remainingMethods(
      self, n: int, k: int, invocations: List[List[int]]
  ) -> List[int]:
    # 1. Build adjacency list
    graph = defaultdict(list)
    for u, v in invocations:
      graph[u].append(v)

    # 2. Find all methods reachable from k using BFS
    reachable = set([k])
    queue = deque([k])

    while queue:
      curr = queue.popleft()
      for neighbor in graph[curr]:
        if neighbor not in reachable:
          reachable.add(neighbor)
          queue.append(neighbor)

    # 3. Check if any node OUTSIDE reachable calls a node INSIDE reachable
    for u, v in invocations:
      if u not in reachable and v in reachable:
        # Cannot remove reachable nodes; return all nodes
        return list(range(n))

    # 4. Return all nodes that are NOT in reachable
    return [i for i in range(n) if i not in reachable]