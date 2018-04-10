from all_functions import *

#data="2+min(31,51,10)-9*max(30,45,11)/mean(1,2,3,4,5)+sd(24,1,5,32)-var(24,1,5,32)"
#data="2+10-9*45/3.0+12.893796958227627-166.25"
#data="5+sin(60)"
#data="5*(-4)"

data = "add([(1,2,3),(1,3,5)],[(1,2,3),(1,3,5)])"

cal=m_calculator(data)
#print(cal.infix())





















#data="2+min(31,51,10)-9*min(30,45,11)"
#list1=list()
#num=''
#
#print(data)
#
#ind = data.find('min')
#while ind != -1:
##if ind !=-1:
#    list1=[]
#    print(ind)
#    expr=data[ind:]
#    while expr[0]!='(':
#        expr=expr.replace(expr[0],'',1)
#    expr=expr.replace(expr[0],'',1)
#    
#    while expr[0]!=')':
#        while expr[0] in ('1234567890.') :
#            num=num+expr[0]
#            expr=expr.replace(expr[0],'',1)
#            print(expr)
#        if expr[0]!=')':
#            expr=expr.replace(expr[0],'',1)
#        list1.append(num)
#        num=''
#        
#    print(list1)
#    expr=expr.replace(expr[0],min(list1),1)
#    #print(expr)
#    data=data[0:ind]+expr
#    print(data)
#    ind = data.find('min')
