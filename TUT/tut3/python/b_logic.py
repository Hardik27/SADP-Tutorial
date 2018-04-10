from all_functions import *

def select(expr):
    if (expr.find('min') or expr.find('max') or expr.find('mean') or expr.find('sd') or expr.find('var')) > -1:
        return s_calculator(expr)
    elif (expr.find('sin') or expr.find('cos') or expr.find('tan')) >= 0 :
        return g_calculator(expr)
    else:
        return b_calculator(expr)
