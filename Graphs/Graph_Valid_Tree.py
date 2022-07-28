class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Union find -> when parent of two nodes that are being unified are the same -> return false 
        #MUST ALSO CHECK TO SEE IF THERE ARE ANY DISJOINT COMPONENTS. this was something I forgot to account for, big mistake.
        
        #next time spend more time making sure I understand all the conditions of my valid case.
        
        
        #3:03 PM start
        #3:45 PM finish
        
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return [0,True]
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return [1,False]
        
        answer = True
        res = n
        for n1,n2 in edges:
            current = union(n1,n2)
            res -= current[0]
            if current[1]:
                return False
            
        if res != 1:
            return False
        
        return answer