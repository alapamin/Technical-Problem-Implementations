#O(nlogk) time complexity -> worst case O(nlogn) if all words are unique
#O(n) space complexity
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import collections
        #check for edge cases -> weird k value or empty array
        if not words or k <= 0:
            return []
        
        #create and fill frequency hash map
        '''
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word,0) + 1
        '''
        frequency = collections.Counter(words)
        
        #create heap
        heap = [(-freq,word) for word,freq in frequency.items()]
        heapq.heapify(heap)
        
        #return top k elements from heap via pop
        answer = []
        for i in range(k):
            pair = heapq.heappop(heap)
            answer.append(pair[1])
            
        return answer