class SparseTable:
    def __init__(self, nums: list[int]):
        self.n = len(nums)
        if self.n == 0:
            self.st = []
            return
            
        self.log_n = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(self.log_n)]
        self.st[0] = list(nums)
        
        for k in range(1, self.log_n):
            length = 1 << (k - 1)
            for i in range(self.n - (1 << k) + 1):
                self.st[k][i] = max(self.st[k - 1][i], self.st[k - 1][i + length])

    def query(self, l: int, r: int) -> int:
        if l > r or not self.st:
            return 0
        k = (r - l + 1).bit_length() - 1
        return max(self.st[k][l], self.st[k][r - (1 << k) + 1])


class Group:
    def __init__(self, start: int, length: int):
        self.start = start
        self.length = length


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        
        # 1. Prefix sum for fast '1' count
        pref_ones = [0] * (n + 1)
        for i in range(n):
            pref_ones[i + 1] = pref_ones[i] + (1 if s[i] == '1' else 0)
            
        def count_ones(l: int, r: int) -> int:
            if l > r:
                return 0
            return pref_ones[r + 1] - pref_ones[l]

        total_ones_s = count_ones(0, n - 1)

        # 2. Extract zero-groups & build correct zero_group_index map
        zero_groups: list[Group] = []
        zero_group_index = [-1] * n
        
        for i in range(n):
            if s[i] == '0':
                if i > 0 and s[i - 1] == '0':
                    zero_groups[-1].length += 1
                else:
                    zero_groups.append(Group(i, 1))
            # CRITICAL: zero_group_index[i] tracks the latest zero group up to index i
            zero_group_index[i] = len(zero_groups) - 1

        num_groups = len(zero_groups)
        
        # If 0 zero-groups exist, no trades can be performed anywhere
        if num_groups == 0:
            return [total_ones_s for _ in queries]

        # 3. Sparse Table over adjacent zero-group combined lengths
        zero_merge_lengths = [
            zero_groups[i].length + zero_groups[i + 1].length
            for i in range(num_groups - 1)
        ]
        st = SparseTable(zero_merge_lengths)

        # 4. Answer each query in O(1)
        ans = []
        for l, r in queries:
            sub_ones = count_ones(l, r)
            outside_ones = total_ones_s - sub_ones
            
            g_l = zero_group_index[l]
            g_r = zero_group_index[r]
            
            # Sub-lengths of zero-groups cut by the boundary
            left = -1
            if s[l] == '0' and g_l != -1:
                left = zero_groups[g_l].length - (l - zero_groups[g_l].start)
                
            right = -1
            if s[r] == '0' and g_r != -1:
                right = r - zero_groups[g_r].start + 1

            start_group = g_l + 1
            end_group = g_r if s[r] == '1' else g_r - 1

            # Query range in sparse table for adjacent pairs: [start_group, end_group - 1]
            start_adj = start_group
            end_adj = end_group - 1

            sub_max = sub_ones  # Baseline: no trade performed

            # Scenario 1: l and r fall in two adjacent zero-groups (spanning over a '1' block)
            if s[l] == '0' and s[r] == '0' and g_l + 1 == g_r:
                sub_max = max(sub_max, sub_ones + left + right)

            # Scenario 2: Range contains fully internal adjacent zero-group pairs
            if start_adj <= end_adj:
                sub_max = max(sub_max, sub_ones + st.query(start_adj, end_adj))

            # Scenario 3: Partial left zero-group + next full zero-group
            if s[l] == '0' and g_l + 1 <= (g_r if s[r] == '1' else g_r - 1):
                sub_max = max(sub_max, sub_ones + left + zero_groups[g_l + 1].length)

            # Scenario 4: Partial right zero-group + previous full zero-group
            if s[r] == '0' and g_l < g_r - 1:
                sub_max = max(sub_max, sub_ones + right + zero_groups[g_r - 1].length)

            ans.append(outside_ones + sub_max)

        return ans