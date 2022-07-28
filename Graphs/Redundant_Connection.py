class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Union Find
        #When parents equal one another when adding a new edge, this is one of the redundant connections
        #Keep saving that to the ans ans you iterate through the edges
        
        #Faster than BFS
        
        par = [i for i in range(len(edges))]
        rank = [1] * len(edges)
        
        def find(n1):
            res = n1
            while par[res] != res:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            
            if p1 == p2:
                return [n1,n2]
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return []
        res = []
        for n1,n2 in edges:
            cN1 = n1 - 1
            cN2 = n2 - 1
            currentAns = union(cN1,cN2)
            if currentAns:
                res = currentAns
                
        return [res[0]+1,res[1]+1]
            
            