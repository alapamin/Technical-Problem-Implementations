class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        def dfs(qOne,qTwo,visited,passes,grid):
            while qOne or qTwo:
                while qOne:
                    currentNode = qOne.popleft()
                    i,j = currentNode[0],currentNode[1]
                    
                    if visited[i][j]:
                        continue
                        
                    visited[i][j] = True
                        
                    #List of pairs of indices ex. [[0,1]...]
                    neighbors = getNeighbors(i,j,grid,visited) 
                    
                    for neighbor in neighbors:
                        qTwo.append(neighbor)        
                if qTwo:
                    passes+=1
                    while qTwo:
                        currentNode = qTwo.popleft()
                        qOne.append(currentNode)
            return passes
                        
        def getNeighbors(i,j,grid,visited):
            #Return a list of lists containing index pairs of valid neighbors
            #Left right up down -> and not visited -> if 1 -> add to neighbors and make rotten
            neighbors = []
            if i > 0 and not visited[i-1][j] and grid[i-1][j] == 1:
                neighbors.append([i-1,j])
                grid[i-1][j] = 2
            if i < len(grid)-1 and not visited[i+1][j] and grid[i+1][j] == 1:
                neighbors.append([i+1,j])
                grid[i+1][j] = 2
            if j > 0 and not visited[i][j-1] and grid[i][j-1] == 1:
                neighbors.append([i,j-1])
                grid[i][j-1] = 2
            if j < len(grid[i])-1 and not visited[i][j+1] and grid[i][j+1] == 1 :
                neighbors.append([i,j+1])
                grid[i][j+1] = 2
            return neighbors
        
        passes = 0 
        isFresh = False
        visited = [[False for value in row] for row in grid]
        qOne,qTwo = deque(),deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    qOne.append([i,j])
                elif not isFresh and grid[i][j] == 1:
                    isFresh = True

        
        passes = dfs(qOne,qTwo,visited,passes,grid)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        
        if not isFresh:
            return 0
        
        return passes
        