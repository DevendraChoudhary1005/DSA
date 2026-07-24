class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        S = list(set(nums))
        
        P = set()
        for i in range(len(S)):
            for j in range(i, len(S)):
                P.add(S[i] ^ S[j])
                
        triplet_xors = set()
        for p in P:
            for c in S:
                triplet_xors.add(p ^ c)
                
        return len(triplet_xors)