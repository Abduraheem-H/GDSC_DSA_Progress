class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators = {
    "/": lambda x, y: int(y / x),  
    "*": lambda x, y: y * x,
    "+": lambda x, y: y + x,
    "-": lambda x, y: y - x
}
        for token in tokens:
            if token in operators:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                result = operators[token](num1, num2)           
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]

        