class Solution:
    #Time : O(n) where n is all the letters in the 2D array. we compare the first word to every other word 
    #Space : O(27 or k) where k is the number of letters in the alphabet which we store in our hashmaps.
    def commonChars(self, words: List[str]) -> List[str]:
        #set of first word
        #for every word besides first -> new set
                  #                   -> for char in seen -> if not in new set -> remove from seen
        
        wordMap = {}
        for word in words[0]:
            for letter in word:
                wordMap[letter] = wordMap.get(letter,0) + 1
                
        answer = []
        if len(words) == 1:
            return ''.split(words)
        
        for i in range(1,len(words)):
            word = words[i]
            newMap = {}
            for letter in word:
                newMap[letter] = newMap.get(letter,0) + 1
                    
            for key in wordMap.keys():
                if key not in newMap:
                    wordMap[key] = 0
                elif wordMap[key] > newMap[key]:
                    wordMap[key] = newMap[key]
                
        
        for letter,freq in wordMap.items():
            if freq > 0:
                for i in range(freq):
                    answer.append(letter)
        
        return answer
        
        