class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #Time complexity : O(n)
        #Space complexity: O(1)
        #Return true if we end up back at 0,0 once instructions are completed
        
        #1,2,3,4 = up,down,left,right
        direction = 1
        location = [0,0]
        #Repeat 4 times because if a sequence is not once valid after 4 repitions, it will never be valid
        for i in range(4):
            for instruction in instructions:
                if instruction == "G":
                    if direction == 1:
                        location[1] += 1
                    elif direction == 2:
                        location[1] -= 1
                    elif direction == 3:
                        location[0] -=1
                    else:
                        location[0] += 1
                elif instruction == "L":
                    if direction == 1:
                        direction = 3
                    elif direction == 2:
                        direction = 4
                    elif direction == 3:
                        direction = 2
                    else:
                        direction = 1
                else:
                    if direction == 1:
                        direction = 4
                    elif direction == 2:
                        direction = 3
                    elif direction == 3:
                        direction = 1
                    else:
                        direction = 2
            if location == [0,0]:
                return True
        return False