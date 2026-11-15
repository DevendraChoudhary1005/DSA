class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        valid_count = 0
        
        for x in arr1:
            # Your idea: Check if ANY element (y) in arr2 falls within the range [x - d, x + d]
            exists_in_range = any((x - d) <= y <= (x + d) for y in arr2)
            
            # If NO element exists in that forbidden range, we keep/count this number!
            if not exists_in_range:
                valid_count += 1
                
        return valid_count