class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        pairs ={
            '}':'{',
            ']':'[',
            ')':'('
        }

        for char in s: 
            if pairs.get(char):
                if stack:
                    if stack[-1] != pairs.get(char):
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(char)
            
        return False if stack else True     