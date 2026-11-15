class Solution:

    def do_it(self,tmp_stack:List[int],operator:str):
        # right operator number
        b = tmp_stack.pop()
        # left operator number
        a = tmp_stack.pop()
        match operator:
            case "+":
                tmp_stack.append(a+b)
            case "-":
                tmp_stack.append(a-b)
            case "*":
                tmp_stack.append(a*b)
            case "/":
                tmp_stack.append(int(a/b))
            case _ :
                raise Exception("unspport")



    def evalRPN(self, tokens: List[str]) -> int:
        tmp_stack = [] 
        for token in tokens:
            match token:
                case "+" | "-" | "*" | "/":
                    self.do_it(tmp_stack,token)
                case number:
                    tmp_stack.append(int(number))
                
        return tmp_stack.pop()