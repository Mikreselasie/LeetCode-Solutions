class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        
        for course,prereq in prerequisites:
            courses[course].append(prereq)
        
        isVisited ={k:0 for k in range(numCourses)}
        GRAY = 1
        BLACK = 2
        isCycle = False

        def dfs(node):
            nonlocal isCycle
            if isCycle:
                return
            
            isVisited[node] = GRAY

            if node in courses:
                for neigh in courses[node]:
                    if isVisited[neigh] == 0:
                        dfs(neigh)
                    elif isVisited[neigh] == GRAY:
                        isCycle = True
            isVisited[node] = BLACK
        ans = None
        for course in range(numCourses):
            if isVisited[course] == 0:
                dfs(course)
                   
        return not isCycle
        


        