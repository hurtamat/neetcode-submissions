class Solution:

    def otherParentheses(self, char) -> str:
        if char == '[':
            return ']'
        elif char == '{':
            return '}'
        elif char == '(':
            return ')'
        else:
            raise Exception("invalid character.")

    def isValid(self, s: str) -> bool:
        if len(s) < 2 or len(s) % 2 == 1:
            return False
        
        stack = []
        cur = 1

        stack.append(s[0])

        for i in range(1, len(s), 1):
            if stack:
                try:
                    other = self.otherParentheses(stack[-1])
                except Exception as e:
                    return False
                if other == s[i]:
                    stack.pop()
                    continue
            
            stack.append(s[i])

        if not stack:
            return True
        else:
            return False


        
        