from calIN import inter

class calculator(inter):
    def __init__(self, expr):
        inter.__init__(self)
        self.expr=list(expr)
        
    def isOp(self,c):
        if c != "": return (c in "+-*/")
        else: return False

    def pri(self,c):
        if c in "+-": return 0
        if c in "*/": return 1

    def isNum(self,c):
        if c != "": return (c in "0123456789.")
        else: return False

    def calc(self,op, num1, num2):
        if op == "+": return str(float(num1) + float(num2))
        if op == "-": return str(float(num1) - float(num2))
        if op == "*": return str(float(num1) * float(num2))
        if op == "/": return str(float(num1) / float(num2))
    
    def infix(self):
        #self.expr = list(self.expr)
        #self.stackChr = list() # character stack
        #self.stackNum = list() # number stack
        #self.num = ""
        while len(self.expr) > 0:
            self.c = self.expr.pop(0)
            if len(self.expr) > 0:
                self.d = self.expr[0]
            else:
                self.d = ""
            if self.isNum(self.c):
                self.num += self.c
                if not self.isNum(self.d):
                    self.stackNum.append(self.num)
                    self.num = ""
            elif self.isOp(self.c):
                while True:
                    if len(self.stackChr) > 0:
                        self.top = self.stackChr[-1]
                    else:
                        self.top = ""
                    if self.isOp(self.top):
                        if not self.pri(self.c) > self.pri(self.top):
                            self.num2 = self.stackNum.pop()
                            self.op = self.stackChr.pop()
                            self.num1 = self.stackNum.pop()
                            self.stackNum.append(self.calc(self.op, self.num1, self.num2))
                        else:
                            self.stackChr.append(self.c)
                            break
                    else:
                        self.stackChr.append(self.c)
                        break
            elif self.c == "(":
                self.stackChr.append(self.c)
            elif self.c == ")":
                while len(self.stackChr) > 0:
                    self.c = self.stackChr.pop()
                    if self.c == "(":
                        break
                    elif self.isOp(self.c):
                        self.num2 = self.stackNum.pop()
                        self.num1 = self.stackNum.pop()
                        self.stackNum.append(self.calc(self.c, self.num1, self.num2))
    
        while len(self.stackChr) > 0:
            self.c = self.stackChr.pop()
            if self.c == "(":
                break
            elif self.isOp(self.c):
                self.num2 = self.stackNum.pop()
                self.num1 = self.stackNum.pop()
                self.stackNum.append(self.calc(self.c, self.num1, self.num2))
    
        return self.stackNum.pop()
