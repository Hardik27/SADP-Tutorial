class inter:
    def __init__(self):
        self.c= ""
        self.op= ""
        self.num1=float()
        self.num2=float()
        self.expr=list()
        self.num=""
        self.stackChr = list() # character stack
        self.stackNum = list() # number stack
        self.d= ""
        self.top = ""

    #Check operator
    def isOp(self,c):
        pass
    
    #prioritty
    def pri(self,c):# operator priority
        pass
    
    #Check number
    def isNum(self,c):
        pass

    def calc(self,op, num1, num2):
        pass

    def infix(self):
        pass
