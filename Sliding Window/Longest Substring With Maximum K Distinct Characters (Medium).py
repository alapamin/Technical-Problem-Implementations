def longest_substring_with_k_distinct(str1, k):
  '''
  Input: String="a[raac]ccccci", K=2
  Output: 2

  windowStart,currentLength = 0,0
  characterCount = {}
  maxLength = float('-inf')

  for loop through the whole string



  We want to use sliding window, where the windowEnd is checked to see whether or
  not our current character is in our hash map

    1. If yes 
    -> maxLength = max(maxLength, windowEnd-windowStart+1)
      add to the hashmap 
    2. If no
    -> add the character to hash map
      if hash map key length > k 
      toRemove = windowStart
        while hashmap[toRemove] > 0
        -> remove windowStart from hashmap
        -> windowStart+=1
      take windowStart character out of hash set

  return maxLength
  '''
  windowStart = 0
  characterCount = {}
  maxLength = float('-inf')

  for windowEnd in range(len(str1)):

    if str1[windowEnd] in characterCount:
      characterCount[str1[windowEnd]] += 1

    else:

      characterCount[str1[windowEnd]] = 1

      while len(characterCount) > k:
        characterCount[str1[windowStart]] -= 1
        if(characterCount[str1[windowStart]] == 0):
          del characterCount[str1[windowStart]]
        windowStart += 1
      
    maxLength = max(maxLength, windowEnd-windowStart + 1)

        
  
  return maxLength


