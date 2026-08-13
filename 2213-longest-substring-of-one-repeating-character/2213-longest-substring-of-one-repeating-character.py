class Node:
    def __init__(self, size=1, char=""):
        self.size = size
        self.pref_char = char
        self.suff_char = char
        self.pref_len = 1 if char else 0
        self.suff_len = 1 if char else 0
        self.max_len = 1 if char else 0

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = list(s)
        self.tree = [Node() for _ in range(4 * self.n)]
        self.build(0, 0, self.n - 1)

    def merge(self, left: Node, right: Node) -> Node:
        res = Node(left.size + right.size, "")
        
        # 1. Calculate the new prefix
        res.pref_char = left.pref_char
        res.pref_len = left.pref_len
        if left.pref_len == left.size and left.pref_char == right.pref_char:
            res.pref_len += right.pref_len
            
        # 2. Calculate the new suffix
        res.suff_char = right.suff_char
        res.suff_len = right.suff_len
        if right.suff_len == right.size and right.suff_char == left.suff_char:
            res.suff_len += left.suff_len
            
        # 3. Calculate the new max length
        res.max_len = max(left.max_len, right.max_len)
        if left.suff_char == right.pref_char:
            res.max_len = max(res.max_len, left.suff_len + right.pref_len)
            
        return res

    def build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = Node(1, self.s[start])
            return
        
        mid = (start + end) // 2
        self.build(2 * node + 1, start, mid)
        self.build(2 * node + 2, mid + 1, end)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, node: int, start: int, end: int, idx: int, char: str):
        if start == end:
            self.tree[node] = Node(1, char)
            self.s[idx] = char
            return
            
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node + 1, start, mid, idx, char)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, char)
            
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        seg_tree = SegmentTree(s)
        ans = []
        
        for i in range(len(queryIndices)):
            seg_tree.update(0, 0, len(s) - 1, queryIndices[i], queryCharacters[i])
            ans.append(seg_tree.tree[0].max_len)
            
        return ans