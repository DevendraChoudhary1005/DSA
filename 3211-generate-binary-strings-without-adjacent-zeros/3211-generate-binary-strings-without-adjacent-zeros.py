class Solution:
    def validStrings(self, n: int) -> List[str]:

        def solve(index, flag, number, result):
            if index>=len(number):
                result.append("".join(number))
                return
            
            number[index] = "1"
            solve(index+1, True, number, result)

            if flag == True:
                number[index] = "0"
                solve(index+1, False, number, result)

        number = ["1"] * n
        result = []
        solve(0, True, number, result)

        return result    
        