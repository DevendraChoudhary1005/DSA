class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        m, n = len(word1), len(word2)
        
        # FIX 1: Initialize with -1. If a suffix can't be matched, 
        # it stays -1, cleanly failing the check later.
        last_possible = [-1] * (n + 1)
        last_possible[n] = m
        
        ptr = m - 1
        for j in range(n - 1, -1, -1):
            while ptr >= 0 and word1[ptr] != word2[j]:
                ptr -= 1
            if ptr >= 0:
                last_possible[j] = ptr
                ptr -= 1
            else:
                break
                
        result = []
        changed = False
        p1 = 0
        
        for p2 in range(n):
            matched = False
            while p1 < m:
                # FIX 2: Always greedily take an exact match
                if word1[p1] == word2[p2]:
                    result.append(p1)
                    p1 += 1
                    matched = True
                    break
                
                # FIX 3: Corrected boundary logic. 
                # Is the latest valid start for the rest of word2 >= our remaining string?
                elif not changed and last_possible[p2 + 1] >= p1 + 1:
                    changed = True
                    result.append(p1)
                    p1 += 1
                    matched = True
                    break
                
                # If neither, we skip this character in word1
                p1 += 1
                
            # If we exhausted word1 without matching word2[p2]
            if not matched:
                return []
                
        return result    