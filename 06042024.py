
o1 = (1/3)
print(f"output is: {o1} type of output:{type(o1)}")

#task1 what is the output of 1/0.0
o2=(1/0)
print(o2) #ZeroDivisionError: float division by zero (Any number can not be divide by zero since we use 0.0 here we recieved float division by zero)

#task2 what would be the output of x * y where x = 100 ; y = None
x=100
y=None
o3 = x*y
print(o3) #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

#task3 what would be the result of the following bool(100) > bool([])
print(bool(100) > bool([])) #(Anything True statement is always greater than False, here bool([]) is empty so it gives False only hence True is greater than False)
#True 

#task4 write a program to convert centigrade to Fahrenheit. The formula is (0°C × 9/5) + 32 = 32°F
celsius = 37
fahrenheit = int((celsius*9/5) + 32)
print(f"farenheit {fahrenheit} is equivalent to {celsius} celsius")

#task5 write a program to convert miles to kilometers
#case 1
mile = 1
kilometers = 1.6
Total_Miles = (mile*kilometers)
print(f"{mile}miles is equivalent to {Total_Miles}kms ")

#case2 using slit to get one decimal in float value
mile = 10
kilometers = 1.6
Total_Miles = (mile*kilometers)
conversion = str(Total_Miles)
Final_output= (conversion.split(".")[0]) +"."+conversion.split(".")[1][0]
print(f"{mile} miles is equivalent to {Final_output} kms ")

#task6 Write a program to evaluate the following expression. (2/3*100 + 23/4)

#As per BODMAS rule, first it is look for bracket in a expression
x=(2/3*100 + 23/4)
#second it will look for Division
y=(2/3) #0.6666666666666666
z=(23/4) #5.75
#third it will look for Multiplication and finally it will perform addition
o3=(0.6666666666666666*100+5.75) # 72.41666666666666