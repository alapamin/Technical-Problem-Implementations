def find_permutation(str1, pattern):
  #If the count of a particular char is over the pattern's count of that char -> 
  #Move windowstart up while       ^^^^^
  charCount = {}
  patternCount = {}
  for char in pattern:
    patternCount[char] = patternCount.get(char,0) + 1
  print(patternCount)

  windowStart,isPattern = 0,False
  for windowEnd in range(len(str1)):
    char = str1[windowEnd]
    charCount[char] = charCount.get(char,0) + 1

    if char not in patternCount:
      charCount.clear()
      while windowStart < windowEnd:
        windowStart+=1
      continue
        
    while charCount[char] > patternCount[char]:
      charCount[char] -= 1
      if charCount[char] == 0:
        del charCount[char]
      windowStart+=1

    if charCount == patternCount:
      isPattern = True
      break

  if charCount == patternCount:
    isPattern = True
    

  print(charCount)
  return isPattern
