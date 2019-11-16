import math


def exhausting_enumeration(x):
    trials = 0
    epsilon = 0.01
    step = 0.00001
    root = 0.0
    while abs(root**2 - x) >= epsilon and root**2 <=x:
        root += step
        trials += 1
    if abs(root**2 - x) >= epsilon:
        print("failed, need to make smaller steps")
    else:
        print("    1) Exhausting_enumeration:")
        print("Number of tries: ", trials,"\n", "square root of ", x, " is ", root)
        print("difference is ", abs(math.sqrt(x) - root) )
    

def bisection_search(x):
    epsilon = 0.01
    trials = 0
    low = 0
    high = max(1.0 , x)
    root = (low + high)/2.0
    while abs(root**2 - x) >= epsilon:
        trials += 1
        if root**2 > x:
            high = root
        else: 
            low = root
        root = (low + high)/2.0
    print("    2) Bisection_search:")
    print("Number of tries: ", trials,"\n", "square root of ", x, " is ", root)
    print("difference is ", abs(math.sqrt(x) - root) )
    



def newton_raphson(x):
    epsilon = 0.01
    root = x/2.0
    trials = 0
    while abs(root**2 - x) >= epsilon:
        trials += 1
        root = root - (root**2 - x)/(2*root)
    print("    2) Newton_Raphson:")
    print("Number of tries: ", trials,"\n", "square root of ", x, " is ", root)
    print("difference is ", abs(math.sqrt(x) - root) )


try: 
    x = float(input())
    exhausting_enumeration(x)
    bisection_search(x)
    newton_raphson(x)
except:
    print("You have to insert a positive real number")


