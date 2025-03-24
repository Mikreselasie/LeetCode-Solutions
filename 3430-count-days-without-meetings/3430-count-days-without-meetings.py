class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x:(x[0],x[1]))

        top = meetings[0][1]
        prev_top = top
        bottom = meetings[0][0]
        meet_dur = top - bottom +1


        # [[1,3],[2,4],[3,5]]    3 1 
        for i in range(1,len(meetings)):
            if meetings[i][0] <= top:
                if meetings[i][1] <= top:
                    continue
                else:
                    top = meetings[i][1]
                    meet_dur += top - prev_top
            else:
                bottom = meetings[i][0]
                top = meetings[i][1]
                meet_dur += top - bottom + 1
            prev_top = top
        return days - meet_dur
