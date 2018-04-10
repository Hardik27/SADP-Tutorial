import threading
from calculator import calculator

class users(threading.Thread):
    count=0
    def __init__(self):
        threading.Thread.__init__(self)
        self.cal=calculator()
        self.problem=list()
        self.result=list()
        self.ans=0.0
        self.expr=""
        users.count=users.count+1;
        
    def run(self):
        self.expr, self.ans = self.cal.get()
        while self.expr != 'q':
            self.problem.append(self.expr)
            self.result.append(self.ans)
            print("Result for ",users.count,": ", self.ans)
            self.expr, self.ans = self.cal.get()
        print(self.problem)
        print(self.result)
        print(users.count)
