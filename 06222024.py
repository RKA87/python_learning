'''
Task 1
Write a function that takes a function and performs the operations like twice, thrice, fource etc.

Ex. increment(fn, 3) 
Should take the respective functions to return twice, thrice etc of the number

'''

def function01(arg1,arg2):
    print("Name:", arg1)
    print("contact No:", arg2)

def function02(arg3):
    print("Project Name:", arg3)

def function03(arg4):
    print("Role:", arg4)

def test_fn(fn,x):
    print("You are calling different function, results will display based on the function that you call")
    return fn(x)

test_fn(function02, "FannieMae")

# +++++++++++++++++++++++++
'''
Task 2
Re-write the above function to return a function that does the same.
'''

def function04():
    print("Checking function without any arguments")

def rewrite(fn):
    return fn

result = (rewrite(function04))
print(result)

'''
Task 3
Write a program to take the function name and parameter as **kwargs and invokes the function with that parameter.  The function and the parameter could be any arbitrary one
'''

def function05(fn,*args):
    print("calling a function by passing parameter as **kwargs")
    return fn, args

x="Task 3 Executed"
y = function05(function02, x)
print(y)




