# 1: evaluate below expression
(2/3*100+23/4)
'''2/3 =0.6666
23/4=5.75
0.6666*100 =66.66
66.66+5.75
=72.41 '''

print (2/3*100+23/4)

#2. Output of 1/0.0
#print (1/0.0)   # zero division error

#3.output of x*y, x=100 ,y=None

#print(100*None)  #unsupported operand type(s) for *: 'int' and 'NoneType'

#4. result of bool(100)>bool([])

print(bool(100)>bool([]))

#5.centigrade to fareheit (0*C x 9/5)+32 =32*F

x= 17
y= (x*9/5)+32
print(f"Celcius {x} to farenheit conversion {y}")

#6.miles to kms conversion 1 mile = 1.6kms

miles= input("enter:")
x= float(miles)
kms =str(x*1.6)

print(type(kms))
print(f"miles{miles}to kms{kms}")


