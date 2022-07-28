class Solution:
    #Time: O(wh)
    #Space: O(wh)
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        from collections import deque
        visited = [[False for value in row] for row in rooms]
        
        q1,q2 = deque(),deque()
        
        def getNeighbors(i,j,rooms):
            neighbors = []
            if i > 0 and rooms[i-1][j] != 0 and rooms[i-1][j] != -1:
                neighbors.append([i-1,j])
            if i < len(rooms)-1 and rooms[i+1][j] != 0 and rooms[i+1][j] != -1:
                neighbors.append([i+1,j])
            if j > 0 and rooms[i][j-1] != 0 and rooms[i][j-1] != -1:
                neighbors.append([i,j-1])
            if j < len(rooms[i])-1 and rooms[i][j+1] != 0 and rooms[i][j+1] != -1:
                neighbors.append([i,j+1])
            return neighbors
        
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    q1.append([i,j])
        
        distance = 0
        while q1 or q2:
            while q1:
                currentNode = q1.popleft()
                i,j = currentNode[0],currentNode[1]
                if visited[i][j]:
                    continue
                    
                visited[i][j] = True
                neighbors = getNeighbors(i,j,rooms)
                
                for neighbor in neighbors:
                    q2.append(neighbor)
                    
            if q2:
                distance+=1
                while q2:
                    currentNode = q2.popleft()
                    i,j = currentNode[0],currentNode[1]
                    
                    rooms[i][j] = min(rooms[i][j],distance)
                    
                    if not visited[i][j]:
                        q1.append(currentNode)
                        
        return rooms
                        
                
        