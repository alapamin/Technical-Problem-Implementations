class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        #Perform DFS when you find an X in the board that is not visited -> make all X neighbors visited
        #10:42 PM start 
        #10:55 PM finish
        visited = [[False for value in row]for row in board]
        ships = 0
        
        def bfs(i,j,visited,board):
            stack = [[i,j]]
            while stack:
                currentNode = stack.pop()
                i,j = currentNode[0],currentNode[1]
                
                if visited[i][j]:
                    continue
                    
                visited[i][j] = True
                neighbors = getNeighbors(i,j,visited,board)
                
                for neighbor in neighbors:
                    stack.append(neighbor)
                    
        def getNeighbors(i,j,visited,board):
            neighbors = []
            if i > 0 and not visited[i-1][j] and board[i-1][j] == 'X':
                neighbors.append([i-1,j])
            if i < len(board)-1 and not visited[i+1][j] and board[i+1][j] == 'X':
                neighbors.append([i+1,j])
            if j > 0 and not visited[i][j-1] and board[i][j-1] == 'X':
                neighbors.append([i,j-1])
            if j < len(board[i])-1 and not visited[i][j+1] and board[i][j+1] == 'X':
                neighbors.append([i,j+1])
            return neighbors
        
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if visited[i][j]:
                    continue
                if board[i][j] == 'X':
                    ships+=1
                    bfs(i,j,visited,board)
        
        return ships