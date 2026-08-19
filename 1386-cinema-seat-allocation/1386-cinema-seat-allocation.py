import collections
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = collections.defaultdict(int)
        for row, seat in reservedSeats:
            reserved[row] |= (1<<seat)

        ans = 2*(n-len(reserved))

        for seats in reserved.values():
            left_free = (seats & 60) == 0
            right_free = (seats & 960) == 0
            middle_free = (seats & 240) == 0

            if left_free and right_free:
                ans += 2
            elif left_free or right_free or middle_free:
                ans += 1

        return ans