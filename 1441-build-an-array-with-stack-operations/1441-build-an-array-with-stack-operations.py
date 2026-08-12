class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        curr_num = 1

        for num in target:
            while curr_num < num:
                result.append("Push")
                result.append("Pop")
                curr_num += 1

            result.append("Push")
            curr_num += 1

        return result