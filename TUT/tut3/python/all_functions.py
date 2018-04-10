from interface import *
import math

class b_calculator(cal_inter):
    def __init__(self, expr):
        cal_inter.__init__(self)
        self.expr=list(expr)
        
    def isOp(self,c):
        if c != "": return (c in "+-*/")
        else: return False

    def pri(self,c):
        if c in "+-": return 0
        if c in "*/": return 1

    def isNum(self,c):
        if c != "":return (c in "0123456789.")
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
        self.num = ""
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


class s_calculator(stat_inter, b_calculator):

    def __init__(self,expr):
        stat_inter.__init__(self)
        b_calculator.__init__(self,expr)
        self.temp=str()
        self.ind=int()
        self.list1=list()
        self.i=int()
        self.temp_l=list()
        self.expr=self.make_list(expr)

    def make_list(self,expr):
        expr= self.min_n(expr)
        expr= self.max_n(expr)
        expr= self.mean(expr)
        expr= self.sd(expr)
        expr= self.var(expr)
        #print(expr)
        return list(expr)

    def search(self, data):
        self.temp_l=[]
        while data[0]!='(':
            data=data.replace(data[0],'',1)
        data=data.replace(data[0],'',1)
        
        while data[0]!=')':
            self.num=''
            while data[0] in ('1234567890.') :
                self.num=self.num+data[0]
                data=data.replace(data[0],'',1)
                #print(data)
            if data[0]!=')':
                data=data.replace(data[0],'',1)
            self.temp_l.append(float(self.num))
        yield self.temp_l
        yield data
    
    def min_n(self,data):
        self.ind = data.find('min')
        while self.ind != -1:
            self.list1=[]
            self.temp=data[self.ind:]

            self.list1, self.temp = self.search(self.temp)
            
            self.temp=self.temp.replace(self.temp[0],str(min(self.list1)),1)
            data=data[0:self.ind]+self.temp
            #print(data)
            self.ind = data.find('min')
        return data
        
    def max_n(self,data):
        self.ind = data.find('max')
        while self.ind != -1:
            self.list1=[]
            self.temp=data[self.ind:]

            self.list1, self.temp = self.search(self.temp)
            
            self.temp=self.temp.replace(self.temp[0],str(max(self.list1)),1)
            data=data[0:self.ind]+self.temp
            #print(data)
            self.ind = data.find('max')
        return data

    def mean(self,data):
        self.ind = data.find('mean')
        while self.ind != -1:
            self.list1=[]
            self.temp=data[self.ind:]

            self.list1, self.temp = self.search(self.temp)
            
            self.num=sum(self.list1) / len(self.list1)
            self.temp=self.temp.replace(self.temp[0],str(self.num),1)
            data=data[0:self.ind]+self.temp
            #print(data)
            self.ind = data.find('mean')
        return data

    def sd(self,data):
        self.ind = data.find('sd')
        while self.ind != -1:
            self.list1=[]
            self.temp=data[self.ind:]

            self.list1, self.temp = self.search(self.temp)
            
            self.num=sum(self.list1) / len(self.list1)
            for self.i in range(0,len(self.list1)):
                self.list1[self.i]=self.list1[self.i]-self.num
                self.list1[self.i]=(self.list1[self.i])*(self.list1[self.i])
            self.num=math.sqrt(sum(self.list1) / len(self.list1))
            self.temp=self.temp.replace(self.temp[0],str(self.num),1)
            data=data[0:self.ind]+self.temp
            #print(data)
            self.ind = data.find('sd')
        return data

    def var(self,data):
        self.ind = data.find('var')
        while self.ind != -1:
            self.list1=[]
            self.temp=data[self.ind:]

            self.list1, self.temp = self.search(self.temp)
            
            self.num=sum(self.list1) / len(self.list1)
            for self.i in range(0,len(self.list1)):
                self.list1[self.i]=self.list1[self.i]-self.num
                self.list1[self.i]=(self.list1[self.i])*(self.list1[self.i])
            self.num=sum(self.list1) / len(self.list1)
            self.temp=self.temp.replace(self.temp[0],str(self.num),1)
            data=data[0:self.ind]+self.temp
            #print(data)
            self.ind = data.find('var')
        return data


class g_calculator(geo_inter, b_calculator):

    def __init__(self,expr):
        geo_inter.__init__(self)
        b_calculator.__init__(self,expr)
        self.temp=str()
        self.ind=int()
        self.expr=self.make_list(expr)

    def make_list(self,expr):
        expr= self.sin(expr)
        expr= self.cos(expr)
        expr= self.tan(expr)
        #print(expr)
        return list(expr)

    def search(self, data):
        self.temp_l=[]
        while data[0]!='(':
            data=data.replace(data[0],'',1)
        data=data.replace(data[0],'',1)

        self.num=''
        while data[0] in ('1234567890.') :
            self.num=self.num+data[0]
            data=data.replace(data[0],'',1)
        data=data.replace(data[0],'',1)

        print(data)
        if len(data)==0:
            data="*"
        
        yield float(self.num)
        yield data
    
    def sin(self,data):
        self.ind = data.find('sin')
        while self.ind != -1:
            self.temp=data[self.ind:]

            self.num, self.temp = self.search(self.temp)
            
            self.num= math.sin(math.degrees(self.num))
            
            self.temp=self.temp.replace(self.temp[0],str(self.num),1)
            data=data[0:self.ind]+self.temp
            #print(data)
            self.ind = data.find('sin')
        return data
    
    def cos(self,data):
        self.ind = data.find('cos')
        while self.ind != -1:
            self.temp=data[self.ind:]

            self.num, self.temp = self.search(self.temp)
            
            self.num= math.cos(math.degrees(self.num))
            
            self.temp=self.temp.replace(self.temp[0],str(self.num),1)
            data=data[0:self.ind]+self.temp
            #print(data)
            self.ind = data.find('cos')
        return data

    def tan(self,data):
        self.ind = data.find('tan')
        while self.ind != -1:
            self.temp=data[self.ind:]

            self.num, self.temp = self.search(self.temp)
            
            self.num= math.tan(math.degrees(self.num))
            
            self.temp=self.temp.replace(self.temp[0],str(self.num),1)
            data=data[0:self.ind]+self.temp
            #print(data)
            self.ind = data.find('tan')
        return data

class m_calculator(mat_inter, b_calculator):
    def __init__(self,expr):
        mat_inter.__init__(self)
        b_calculator.__init__(self,expr)
        self.temp=str()
        self.ind=int()
        self.list1=list()
        self.list2=list()
        self.dum=list()
        self.temp_1=list()
        self.temp_2=list()
        self.expr=self.make_list(expr)

    def make_list(self,expr):
        expr= self.add(expr)
        #expr= self.sub(expr)
        #expr= self.mul(expr)
        #expr= self.trans(expr)
        print(expr)
        return list(expr)

    def search(self, data):
        while data[0] !=']':
            data=data.replace(data[0],'',1)
            self.temp_l=[]
            while data[0]!='(':
                data=data.replace(data[0],'',1)
            data=data.replace(data[0],'',1)
            
            while data[0]!=')':
                self.num=''
                while data[0] in ('1234567890.') :
                    self.num=self.num+data[0]
                    data=data.replace(data[0],'',1)
                    #print(data)
                if data[0]!=')':
                    data=data.replace(data[0],'',1)
                self.dum.append(float(self.num))
        self.temp_1.append(self.dum)    
        yield self.temp_1
        #yield self.temp_2
        yield data

    def add():
        self.ind = data.find('add')
        while self.ind != -1:
            self.temp=data[self.ind:]

            self.list1, self.temp = self.search(self.temp)
            self.temp=self.temp.replace(self.temp[0],'',1)
            self.list2, self.temp = self.search(self.temp)

            
            
            self.temp=self.temp.replace(self.temp[0],str(self.num),1)
            data=data[0:self.ind]+self.temp
            #print(data)
            self.ind = data.find('tan')
        return data
    def infix(self):
        #self.expr = list(self.expr)
        #self.stackChr = list() # character stack
        #self.stackNum = list() # number stack
        self.num = ""
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
