class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [[] for i in range(numCourses)]
        incoming = [0]*numCourses
        queue = deque()
        sorted_arr = []

        for course,pre in prerequisites:
            courses[pre].append(course)
            incoming[course] += 1

        print(courses)
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            sorted_arr.append(course)

            for val in courses[course]:
                incoming[val] -= 1
                if incoming[val] == 0: 
                    queue.append(val)     
        if len(sorted_arr) != numCourses: return []
        return sorted_arr 