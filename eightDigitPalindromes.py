#Generate all 8 digit palindromes in O(1) time and O(1) space complexity (most efficient way possible)

#Solution by Mohammad Amin:

#Mirror and add every 4 digit number starting from 1000 
#Without the usage of concactenation (higher efficiency) 

for x in range(1000,10000):
    answer = x
    splitter = x
    
    #Mirroring the current number and adding that mirror to the number, creating a palindrome
    for i in range(4):
        
        modAnswer = splitter%10
        
        answer = (answer*10) + modAnswer
        
        splitter= splitter //10
        
    print(answer) 
