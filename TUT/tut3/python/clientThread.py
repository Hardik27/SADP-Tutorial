import threading
import socket

from interface import *
#from all_functions import *
import b_logic

class clientThread(threading.Thread):
    def __init__(self,con):
        threading.Thread.__init__(self)
        self.cal= cal_inter()
        self.c=con
        #print("Connection!")
        self.summary={}
        self.res=0.0
        self.data=""
    def run(self):
        while True:
            # data received from client
            self.data = self.c.recv(1024).decode('utf-8')      
            if self.data== "q":
                break;
            self.cal=b_logic.select(self.data)
            #self.cal=g_calculator(self.data)
            self.res=self.cal.infix()

            self.summary[self.data]=self.res
            # send back reversed string to client
            self.c.send(self.res.encode('utf-8'))

        #self.c.send(self.summary.encode('utf-8'))

        # connection closed
        self.c.close()
