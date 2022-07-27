class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque
        
        def dfs(pair, setType, heights, visited):
            queue = deque()
            
            queue.append(pair)
            
            while queue:
                currentNode = queue.popleft()
                
                
                i = currentNode[0]
                j = currentNode[1]
                if visited[i][j]:
                    continue
                    
                #print(currentNode)
                    
                visited[i][j] = True
                
                if tuple(currentNode) not in setType:
                    setType.add(tuple(currentNode))
                
                neighbors = getNeighbors(currentNode,visited,heights) #checks if neighbors are seen, if they're existant positionally, and if they're >= value
                
                for neighbor in neighbors:
                    queue.append(neighbor)
        
        def getNeighbors(pair,visited,heights):
            neighbors = []
            i,j = pair[0],pair[1]
            #print(i,j)
            if i > 0 and not visited[i-1][j] and heights[i-1][j] >= heights[i][j]:
                neighbors.append([i-1,j])
            if i < len(heights)-1 and not visited[i+1][j] and heights[i+1][j] >= heights[i][j]:
                neighbors.append([i+1,j])
            if j > 0 and not visited[i][j-1] and heights[i][j-1] >= heights[i][j]:
                neighbors.append([i,j-1])
            if j < len(heights[i])-1 and not visited[i][j+1] and heights[i][j+1] >= heights[i][j]:
                neighbors.append([i,j+1])
            return neighbors
                
                
        
        
        
        pacific = [[0,i] for i in range(len(heights[0]))] + [[i,0] for i in range(len(heights))]
        atlantic = [[len(heights)-1,i] for i in range(len(heights[-1]))] + [[i,len(heights[i])-1] for i in range(len(heights))]
        visited = [[False for value in row] for row in heights]
        
        tPacific = tuple(map(tuple, pacific))
        tAtlantic = tuple(map(tuple, atlantic))

        pSet,qSet = set(tPacific),set(tAtlantic)
        
        
        for pair in pacific:
            dfs(pair, pSet, heights, visited)
            
        print('Second half')
        visited = [[False for value in row] for row in heights]
        for pair in atlantic:
            dfs(pair, qSet,heights, visited)
            
            
        print(pSet)
        print(qSet)
        ans = []
        
        for pair in pSet:
            if pair in qSet:
                ans.append(pair)
                
        return ans
    
        
        
        
        
        
        
        