class Solution:
    def frequencySort(self, s: str) -> str:
        import heapq
        import collections
        #Time complexity if all char are unique -> O(nlogn)
        #Space complexity O(n)
        
        frequencies = collections.Counter(s)
        
        heap = []
        for num,freq in frequencies.items():
            heapq.heappush(heap,(-freq,num))
        
        answer = []
        while heap:
            current = heapq.heappop(heap)
            count = current[0]
            while count < 0:
                count+=1
                answer.append(current[1]) 
            
        
        return ''.join(answer)

  