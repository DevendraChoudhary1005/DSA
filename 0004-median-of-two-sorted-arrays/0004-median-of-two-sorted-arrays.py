class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        i, j = 0, 0
        merged = []
    
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
            
        merged.extend(arr1[i:])
        merged.extend(arr2[j:])

        n = len(merged)

        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[(n // 2) - 1] + merged[n // 2]) / 2.0