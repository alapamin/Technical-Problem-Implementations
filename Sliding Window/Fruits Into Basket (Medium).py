#Solution by Mohammad Amin

def fruits_into_baskets(fruits):
  fruitMap = {}
  windowStart = 0
  maxFruits = float('-inf')
  currentFruits = 0

  for windowEnd in range(len(fruits)):

    endFruit = fruits[windowEnd]

    if endFruit in fruitMap:
      fruitMap[endFruit] += 1
      #print(fruitMap)
    else:
      fruitMap[endFruit] = 1
      #print("First add: ",fruitMap)
      
      while len(fruitMap) > 2:
        beginningFruit = fruits[windowStart]

        fruitMap[beginningFruit] -= 1

        if fruitMap[beginningFruit] == 0:
          del fruitMap[beginningFruit]

        windowStart+=1
        print(fruitMap)
    
    maxFruits = max(maxFruits, windowEnd-windowStart+1)



  return maxFruits