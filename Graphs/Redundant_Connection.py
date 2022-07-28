class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Run union find
        #If when finding union if rank[p1] == 2 or rank[p2] == 2 -> set answer to edge
        par = [i for i in range(0,len(edges))]
        rank = [1 for i in range(0,len(edges))]
        
        def find(n1):
            res = n1
            while par[res] != res:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            
            if p1==p2:
                return [n1,n2] #Any time we create a union between two nodes who already have the same parent -> this is the 3rd added edge.
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2]+=rank[p1]
            else:
                par[p2] = p1
                rank[p1]+=rank[p2]
            return []
        
        ans = []
        for i in range(len(edges)):
            for j in range(len(edges[i])):
                edges[i][j]-=1
                
        for n1,n2 in edges:
            current = union(n1,n2)
            if len(current) == 2:
                ans = current
        ans[0]+=1
        ans[1]+=1
        return ans
                