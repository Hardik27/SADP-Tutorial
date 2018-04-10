class cal_inter:
    
    def __init__(self):
        self.c= ""
        self.op= ""
        self.num1=0
        self.num2=0
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

class stat_inter(cal_inter):

    def __init__(self):
        cal_inter.__init__(self)

    def make_list(self,expr):
        pass

    def mean(self,expr):
        pass

    def sd(self,expr):
        pass

    def var(self,expr):
        pass

    def min_n(self,expr):
        pass

    def max_n(self,expr):
        pass

class geo_inter(cal_inter):
    def __init__(self):
        cal_inter.__init__(self)

    def search(self,expr):
        pass

    def make_list(self,expr):
        pass

    def sin(self,expr):
        pass

    def cos(self,expr):
        pass

    def tan(self,expr):
        pass


class mat_inter(cal_inter):
    def __init__(self):
        cal_inter.__init__(self)

    def search(self,expr):
        pass

    def make_list(self,expr):
        pass

    def transpose(self,expr):
        pass
