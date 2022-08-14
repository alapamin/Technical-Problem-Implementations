class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        import heapq
        import collections
        #Time complexity: O(nlogn) worst case if all elements are unique -> beacuse of heapify & heappop
        #Space complexity: O(n) for hashmaps and heap
        

        #Distance from origin, point one will always be 0,0
        def calculateDistance(p1,p2):
            xPow = pow(p1[0]-p2[0],2)
            yPow = pow(p1[1]-p2[1],2)
            return abs(math.sqrt(xPow+yPow))
        
        #Frequency hash map of the amount of times a point occurs
        frequencies = {}
        
        #Make all points a tuple and put them into a hashmap of (x,y) : distance from origin
        distanceMap = {}
        origin = (0,0)
        for point in points:
            currentPoint = tuple(point)
            distanceMap[currentPoint] = calculateDistance(origin,currentPoint)
            frequencies[currentPoint] = frequencies.get(currentPoint,0) + 1
        
        
        #Make a heap containing all tuples & their distance from origin
        #heapify
        heap = [(distance,point) for point,distance in distanceMap.items()]
        heapq.heapify(heap)
        
        #return top k elements of heap (min heap -> so closest values will come first)
        answer = []
        for _ in range(k):
            #If point at in frequency map occurs more than once -> add to answer, and subtract 1 from count
            currentPoint = heap[0]
            if frequencies[currentPoint[1]] > 1:
                answer.append(list(currentPoint[1]))
                frequencies[currentPoint[1]]-=1
                continue
                
            currentPoint = heapq.heappop(heap)
            answer.append(list(currentPoint[1]))
        return answer
        