class Solution:
    def isValid(self, s: str) -> bool:
        hash_table = {"]": "[", ")": "(", "}": "{"}
        stack = []

        
        if s and s[0] in hash_table:
            return False
        
        for char in s:
            if char in hash_table:  
                if stack and stack[-1] == hash_table[char]:  
                    stack.pop()  
                else:
                    return False 
            else:  
                stack.append(char)

        return not stack  
