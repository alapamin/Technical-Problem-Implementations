class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def getNeighbors(i,j,grid,visited):
            neighbors = []
            if i > 0 and grid[i-1][j] == 1 and not visited[i-1][j]:
                neighbors.append([i-1,j])
            if i < len(grid)-1 and grid[i+1][j] == 1 and not visited[i+1][j]:
                neighbors.append([i+1,j])
            if j > 0 and grid[i][j-1] == 1 and not visited[i][j-1]:
                neighbors.append([i,j-1])
            if j < len(grid[i])-1 and grid[i][j+1] == 1 and not visited[i][j+1]:
                neighbors.append([i,j+1])
            return neighbors

        def countIslandSize(i,j,grid,visited):
            stack = [[i,j]]
            currSize = 0
            while stack:
                currentNode = stack.pop()
                i = currentNode[0]
                j = currentNode[1]

                if visited[i][j]:
                    continue

                visited[i][j] = True

                currSize+=1
                neighbors = getNeighbors(i,j,grid,visited)
                for neighbor in neighbors:
                    stack.append(neighbor)
            return currSize
    
        visited = [[False for value in row] for row in grid]
        maxSize = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j]:
                    continue
                if grid[i][j] != 1:
                    continue
                maxSize = max(countIslandSize(i,j,grid,visited),maxSize)
        return maxSize
    
    