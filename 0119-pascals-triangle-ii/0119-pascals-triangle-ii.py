class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [1]*(rowIndex+1)
        base = factorial(rowIndex)
        for i in range(1,rowIndex):
            answer[i] = base //(factorial(i)*factorial(rowIndex-i))

        def fatorial(x):
            y = 1
            while x > 1:
                y *= x
                x -= 1
            return y
        return answer
        