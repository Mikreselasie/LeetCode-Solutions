class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstPtr = 0
        secondPtr = 0
        answer = []

        while firstPtr < len(firstList) and secondPtr < len(secondList):
            top = min(firstList[firstPtr][1],secondList[secondPtr][1])
            bottom = max(firstList[firstPtr][0],secondList[secondPtr][0])

            if top >= bottom:
                answer.append([bottom,top])
            if top == firstList[firstPtr][1]:
                firstPtr += 1
            else:
                secondPtr += 1
        return answer


