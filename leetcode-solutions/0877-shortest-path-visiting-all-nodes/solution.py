class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        length=len(graph)
        full_mask=(1<<length)-1
        visited=[[False]*(1<<length) for i in range(length)]
        queue=deque()

        for j in range(length):
            mask=1<<j
            queue.append((j,mask,0))
            visited[j][mask]=True
        while queue:
            node,mask,dist=queue.popleft()
            if mask==full_mask:
                return dist
            for k in graph[node]:
                new_mask=mask|(1<<k)
                if not visited[k][new_mask]:
                    visited[k][new_mask]=True
                    queue.append((k,new_mask,dist+1))
        return 0
