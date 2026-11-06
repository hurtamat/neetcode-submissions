class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []


        for op in tokens:
            if (op == '+' or op == '-' or op == '*' or op == '/'):
                b = stack.pop()
                a = stack.pop()

                if op == '+':
                    stack.append(a + b)
                elif op == '-':
                    stack.append(a - b)
                elif op == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
                continue
            
            stack.append(int(op))
            
        return stack[-1]
            
            
                
            

        