class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                idx = stack.pop()[1]
                answer[idx] = i - idx
            stack.append([temperatures[i],i])
        return answer
        