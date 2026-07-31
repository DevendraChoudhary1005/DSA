from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:

        freq = Counter(word)
        sorted_freq = sorted(freq.values(), reverse = True)
        pushes = 0 

        for i in range(len(sorted_freq)):
            count = sorted_freq[i]
            cost_per_pushes = (i//8)+1
            pushes += count*cost_per_pushes

        return pushes