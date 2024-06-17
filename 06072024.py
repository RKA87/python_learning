# Task 1
# Given an integer, perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of 1 to 10, print Not Weird
# If  is even and in the inclusive range of 11 to 20 , print Weird
# If  is even and greater than 20, print Not Weird

number = int(input("Enter the Number:"))
x=(number%2)

#case1
if x==0 and number<=10:
    print("print Not Weird")

if (x==0) and (number >10 and number <20):
    print("print Weird")


if (x==0) and (number >20):
    print("print Not Weird")

#case2
if (x==0):
    if (number<=10):
        print("print Not Weird")
    elif (number >10 and number <=20):
        print("print Weird")
    elif (number >20):
        print("print Not Weird")
elif(x!=0):
    print("Given Input is Odd, weird print")    

#  Write a Python program to calculate a dog's age in dog years.
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output:
# Input a dog's age in human years: 15                                    
# The dog's age in dog's years is 73

y = int(input("Enter Dog Age:"))
x=y
if y <= 2:
    dog_age = (2*10.5)  
    print(dog_age)

if y >2:
    dog_age1 = (y-2)*4
    dog_age1=dog_age1+(2*10.5)
    print(dog_age1)
    print("Input a dog's age in human years:", x)
    print("The dog's age in dog's years:", dog_age1)

#Task 3 Print all the numbers between 100 to 150

for i in range(100,150):
    print(i)

#Task 4 Print all the numbers between 150 to 200 that are not divisible by 10
for i in range(150,200):
    if (i%2)!=0:
        print(i)

#Task 5 print all the numbers between -50 to 0 in intervals of 5
for i in range (-50, 0, 5):
    print(i)

#Task 6 Print all the even numbers between 2 numbers. The 2 numbers should be accepted from the user.

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))

for i in range(x,y,2):
    print(i)

#Task 7 print the letters ‘a’ to ‘z’ using for loop.  

#Task 8 Print every letter of the string “Rainbow children” using a for loop
x="Rainbow children"
for i in x:
    print(x)

#Task 9 Print the letters of the word in “Welcome Python” in the reverse order
y="Welcome Python"

for i in range(0,len(y)):
    i = -i-1
    print(y[i])

#case 2
add=(len(y)+1)
for i in range(1,add):
    print(y[-i])

#case 3
print(y[::-1])

#Task 10 Print the square of the numbers between 2 to 20
for i in range(2,20):
    output= i*i
    print("For Number:",i, "Output:", output)


for i in range(2,20):
    print(i)

# Task 11
# Print the numbers that are divisible by both 5 and 10 between 1 and 100
for i in range(1,101):
    if (i%5==0) and (i%10==0):
        print(i)


# Task 12 
# Print the multiplication table for the number 5 (up to 5 x 10 = 50)
for i in range(1,11):
    print("5","x",i,"=",5*i)

# Task 13
# A common formula for calculating weight is as follows: 
# Men: IBW (kgs) = 22 × (height in meters)
# Women: IBW (kgs) = 22 × (height in meters − 10 cm)
# Print the weight for the heights starting from 1 meter for both Men and Women

men_input = int(input("Enter man height in meters:"))
women_input = int(input("Enter women height in meters:"))

for i in range(1, men_input+1):
    men_weight = (i*22)
    print("Men Weight for height number", i, "is equivanlent to", men_weight)

for j in range(1,women_input+1):
    women_input = (22*(j-0.1))
    print("Women Weight for height number", j, "is equivanlent to", women_input)


#case 2

var1 = 1
while var1!=(men_input+1):
    men_weight = (var1*22)
    print("Men Weight for height number", var1, "is equivanlent to", men_weight)
    var1 +=1


#Task 14 - Extended to Task13

men_input = int(input("Enter height in meters:"))
women_input = int(input("Enter height in meters:"))

for i in range(1, men_input+1):
    men_weight = (i*22)
    print("Men Weight for height number", i, "is equivanlent to", men_weight)
    kg = men_weight
    m2 = (i*i)
    bmi = kg/m2
    if (bmi >= 18.5 and bmi <= 24.9):
        print(" BMI is in healthy range")
    elif(bmi >= 25):
        print("BMI is overweight")
    else:
        print("BMI range is less weight")

for j in range(1,women_input+1):
    women_weight = (22*(j-0.1))
    print("Women Weight for height number", j, "is equivanlent to", women_weight)
    kg = women_weight
    m2 = (i*i)
    bmi = kg/m2
    if (bmi >= 18.5 and bmi <= 24.9):
        print(" BMI of women is in healthy range")
    elif(bmi >= 25):
        print("BMI of women is overweight")
    else:
        print("BMI of women range is less weight")

#Task15 Write a Python program to convert a month name to a number of days

month_name = ["July", "Aug", "Sept", "Oct", "Nov", "Dec"]

m1 = ["Jan", "Mar", "May", "July", "Aug", "Oct", "Dec"]

m2 = ["Apr", "June", "Sept", "Nov" ]

m3 = ['Feb']

month_input = input("Enter Month Name:")

if month_input in m1:
    print("After Coversion: 31 days")

if month_input in m2:
    print("After Coversion: 30 days")

if month_input in m3:
    print("After Conversion: 28 days")

#Task16 Write a Python program to find the median of three values.
# Expected Output:
# Input first number: 15                                                  
# Input second number: 26                                                 
# Input third number: 29                                                  
# The median is 26.0

n1 = (input("Enter first number:"))
n2 = (input("Enter second number:"))
n3 = (input("Enter third number:"))

n =(n1 +","+n2+","+n3)
x=(n.split(','))
tot_numbers = len(x)
print(tot_numbers)

# if (tot_numbers%2)==0:
#     median = int(tot_numbers/2)
#     print("Median Number:", x[median])

median = (len(x)+1)/2
print("Median Number:", x[int(median)-1])

# Write a Python program to check if a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Expected Output:
# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle 

x = int(input("Enter 01 numnber:"))
y = int(input("Enter 02 numnber:"))
z = int(input("Enter 03 numnber:"))

if x==y==z:
    print("Its Equilateral triangle")
elif (x==y) or (y==z) or (x==z):
    print("It's Isosceles triange which has two equal sides")
else:
    print("Its a Scalene triangle which has un-equal sides")