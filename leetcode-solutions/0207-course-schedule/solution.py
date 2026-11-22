class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]
        degree=[0]*numCourses

        for c1,c2 in prerequisites:
            adj[c2].append(c1)
            degree[c1]+=1
        queue=deque(i for(i,d) in enumerate(degree) if d==0)
        visited=0
        while queue:
            c1=queue.popleft()
            visited+=1
            for dep in adj[c1]:
                degree[dep]-=1
                if not degree[dep]:
                    queue.append(dep)
        return visited==numCourses
