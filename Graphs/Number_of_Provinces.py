class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #O(n) time complexity -> only go through every row 1 time 
        #O(n) space complexity -> store queue and seen map
        '''
        [1,1,0,1], 
        [1,1,0,0],
        [0,0,1,0]
        [1,0,0,0]
        
        copy seen matrix of all false 
        
        Iterate through row -> if row not seen -> make seen -> add all values in row to stack & count+=1
        
        
        DFS:
            is value 0? -> yes -> continue
            is row @ j INDEX seen? -> yes -> continue
                            -> no -> make it seen 
                            
            
            add row @ j to stack
            
        
        get neighbors:
            is value 1 and not seen (left and right) -> add to neighbors
            -> return neighbors
            -> add flipped value to stack as well
        '''
        from collections import deque
        def getNeighbors(j,queue,matrix,seen):
            neighbors = []
            for i in range(len(matrix)):
                if matrix[j][i] == 1:
                    neighbors.append([j,i])
            print("Neighbors: ", neighbors)
            return neighbors
        
        def bfs(queue,matrix,seen):
            print(seen)
            while queue:
                currentNode = queue.popleft()
                i,j = currentNode[0],currentNode[1]
                
                if matrix[i][j] == 0:
                    continue
                if seen[j]:
                    continue
                
                seen[j] = True
                
                neighbors = getNeighbors(j,queue,matrix,seen)
                for neighbor in neighbors:
                    queue.append(neighbor)

        matrix = isConnected
        seen = [False for row in matrix]
        queue = deque()
        count = 0
        
        for i in range(len(matrix)):
            
            #If this is a new province (row) -> add to count, else go to next province (row)
            if not seen[i]:
                count+=1
            else:
                continue
                
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    queue.append([i,j])
            print(queue)
                    
            
            if not seen[i]:
                seen[i] = True
                bfs(queue,matrix,seen)
                
        return count
    
        
            
            
        
        
        