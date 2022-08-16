from typing import List

#O(n!) time complexity -> generating permutations (n-1,n-2,n-3...)
#O(n!) space -> storing permutations
def permutations(letters: str) -> List[str]:
    ans = []
    seen = [False for letter in letters]
    def dfs(cPath,seen):
        if len(cPath) == len(letters):
            ans.append(''.join(cPath))
        for i,char in enumerate(letters):
            if seen[i]:
                continue
            seen[i] = True
            cPath.append(char)
            dfs(cPath,seen)
            cPath.pop()
            seen[i] = False
    dfs([],seen)
    return ans        
        

if __name__ == '__main__':
    letters = input()
    res = permutations(letters)
    for line in res:
        print(line)
