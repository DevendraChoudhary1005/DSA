from collections import Counter
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_count = Counter(s)

        prefix_count = Counter()
        can_match_prefix = [True]*(n+1)

        for idx in range(n):
            prefix_count[target[idx]] += 1

            if prefix_count[target[idx]] > total_count[target[idx]]:
                for k in range(idx+1, n+1):
                    can_match_prefix[k] = False

                break

        for i in range(n-1, -1, -1):
            if not can_match_prefix[i]:
                continue

            rem_count = total_count.copy()
            for k in range(i):
                rem_count[target[k]] -= 1

            target_char = target[i]
            possible_char = sorted([c for c in rem_count if rem_count[c] > 0 and c > target_char])

            if possible_char:
                chosen_char = possible_char[0]
                rem_count[chosen_char] -= 1

                suffix = []

                for c in sorted(rem_count.keys()):
                    suffix.append(c*rem_count[c])

                return target[:i] + chosen_char + "".join(suffix)

        return ""