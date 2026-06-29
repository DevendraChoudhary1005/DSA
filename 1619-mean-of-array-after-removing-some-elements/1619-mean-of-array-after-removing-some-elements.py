class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)

        arr.sort()

        k = int(n *  0.05)

        remaining_arr = arr[k: n-k]

        return sum(remaining_arr)/len(remaining_arr)