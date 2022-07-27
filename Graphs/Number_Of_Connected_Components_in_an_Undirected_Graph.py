class Solution:
    #Time: O(v+e)
    #Space: O(v+e)
    #Union find is better time complexity.
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import deque
        
        ans = 0
        adjacencyList = {i:[] for i in range(n)}
        
        for n1,n2 in edges:
            adjacencyList[n1].append(n2)
            adjacencyList[n2].append(n1)
            
        visited = [False for i in range(n)]
        queue = deque()
        
        for key in adjacencyList.keys():
            if not visited[key]:
                ans+=1
                queue.append(key)
                while queue:
                    currentNode = queue.popleft()
                    visited[currentNode] = True
                    for child in adjacencyList[currentNode]:
                        if not visited[child]:
                            queue.append(child)
        
        return ans