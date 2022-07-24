class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverseIsland(i,j,grid,visited):
            stack = [[i,j]]
            while stack:
                currentNode = stack.pop()
                i,j = currentNode[0],currentNode[1]
                
                if visited[i][j]:
                    continue
                visited[i][j] = True
                if grid[i][j] == '0':
                    continue
                
                neighbors = traverseNeighbors(i,j,grid,visited)
                
                for neighbor in neighbors:
                    stack.append(neighbor)
                    
        def traverseNeighbors(i,j,grid,visited):
            neighbors = []
            if i > 0 and not visited[i-1][j] and grid[i-1][j] == '1':
                neighbors.append([i-1,j])
            if i < len(grid)-1 and not visited[i+1][j] and grid[i+1][j] == '1':
                neighbors.append([i+1,j])
            if j > 0 and not visited[i][j-1] and grid[i][j-1] == '1':
                neighbors.append([i,j-1])
            if j < len(grid[i])-1 and not visited[i][j+1] and grid[i][j+1] == '1':
                neighbors.append([i,j+1])
            return neighbors
        
        numOfIslands = 0
        visited = [[False for value in row] for row in grid]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j]:
                    continue
                if grid[i][j] == '0':
                    continue
                traverseIsland(i,j,grid,visited)
                numOfIslands+=1
        return numOfIslands
        