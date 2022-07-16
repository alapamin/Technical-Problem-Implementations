def cycleInGraph(edges):
    #Topological sort -> if len(edges) == ansArray -> Return False (no cycle)
    
    #Number of incoming edges for i? 
    #Adjacency list is given
    inEdges = {i:0 for i in range(len(edges))}

    #Populate inEdges
    for vertex in edges:
        for child in vertex:
            inEdges[child]+=1

    from collections import deque

    sources = deque()
    for key in inEdges.keys():
        if inEdges[key] == 0:
            sources.append(key)

    ansArr = []
    while sources:
        vertex = sources.popleft()
        ansArr.append(vertex)
        for child in edges[vertex]:
            inEdges[child]-=1
            if inEdges[child] == 0:
                sources.append(child)

    return len(ansArr) != len(edges)

    