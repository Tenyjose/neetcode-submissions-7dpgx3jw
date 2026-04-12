class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        operators= ['*',"/","+","-"]
        for token in tokens:
            if token not in operators:
                stack.append(int(token))

            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    res = a+b
                if token == "-":
                    res = a-b
                if token == "*":
                    res = a*b
                if token == "/":
                    res = int(a/b)
                
                stack.append(res)
        return stack[0]


