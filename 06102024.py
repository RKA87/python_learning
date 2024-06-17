# Task 1
# The requirement is to spend money from a piggy bank until there is none left, however, you can only spend Rs.10 at a time.
# You will have Rs.100 to start with. Each time you spend money, you will print the remaining amount of money left in the piggy bank.

counter = 0
print("Total Amount: 100")
for i in range(90,0,-10):
    counter +=1
    print("Remaning Amount After Each Counter:", counter,"--> Time Spent_Remaining Amount:", i)

#Task 3 Print the letters of the word “Himalayan Wild” in separate line

x="Himalayan Wild"
for i in x:
    print(i)

# Task 4
# Write a program to list all the number divisible by both 3 and 5 using while loop.  
# Rewrite the program using for loop

# case 1
for i in range(1,100):
    if (i%3==0) and (i%5)==0:
        print(i)

end_number = int(input("Enter Number:"))
start_number = 1

# case 2
while start_number <= end_number:
    if ((start_number%3==0)and(start_number%5)==0):
        print(start_number)
    start_number +=1

# Task 5
# Write a program that prints the numbers from 0 to 100 in the reverse order using while loop

#case 1
for i in range(100,0,-1):
    print(i)

#case 2
start_number = 100
end_number = 0

while start_number >= end_number:
    print(start_number)
    start_number -= 1

#Task 6 Write a program to display the half value of each number from 1 to 100.
for i in range(1,100):
    x=(i/2)
    print(x)

# Task 7
# Write a program to display the square of the number entered by the user till the user enters “Quit”

inp = (input("Enter a Number:"))

#case 1
number = float(inp)
print(number)

if type(inp) == str:
    if inp == "Quit":
        print("progarm quit")

if number == float:
    x=number*number
    print(x)

#case 2

while inp != "Quit":
    number = float(inp)
    x=(number*number)
    print(x)

# Task 8
# Writing a guessing game that will allow inputs from the user to guess the color of a Bird. A maximum of 3 attempts is permitted. If the user fails to guess correctly in 3 attempts, 
# ask him to try again and exit. If the guess is right print “Right guess” else print “Wrong guess”.  The program should support about 3-4 birds.

# Task 9
#Write a guessing game in which the user enters a number and you should tell if the number the user guessed is less than or greater than the target number. 
# If the guess if correct “Say correct guess”

number=int(input("Enter a Number:"))

target_number = 10000

if (number < target_number) or (number > target_number):
    print("Say Correct guess")
else:
    print("Guess Number not match with Target Number")

# Task 10
# Analyze and try out the code related to patterns generated using while and 
# for loop at https://pynative.com/print-pattern-python-examples/.

#pattern output
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

rows = 5

for i in range(1,rows+1):
    for j in range(i):
        print(i, end="")
    print("")

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = "")
    print(" ")

#Inverted Patttern
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5
b = 0
for i in range(5,0,-1):
    b +=1
    for j in range(1, i+1):
        print(b, end=' ')
    print(" ")

# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5
rows = 5
num = 5

for i in range(6,0,-1):
    for j in range(i):
        print(num, end= " ")
    print(" ")

# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1

for i in range(rows,0,-1):
    for j in range(i+1):
        print(j, end = " ")
    print(" ")

# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9

for i in range(1,6):
    x=(i*2)-1
    for j in range(i+1):
        print(x, end=" ")
    print(" ")

# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1

rows = 5
for i in range(rows,0, -1):
    for j in range(i):
        print(i, end=" ")
    print(" ")

# 1
# 2 3
# 4 5 6
# 7 8 9 10

for i in range(5):
    x = i +1
    for j in range(i):
        print(x, end = " ")
    print(" ")

#           1  
#         1 2
#       1 2 3
#     1 2 3 4
#   1 2 3 4 5

for i in range(1,6):
    num=1
    for j in range(6,0,-1):
        if j > i:
            print(" ", end=" ")
        else:
            print(num, end=" ")
    print(" ")

# 1
# 2 3
# 4 5 6
# 7 8 9 10
num =1
for i in range (1,5):
    for j in range(0,i):
        print(num, end="")
        num += 1
    print(" ")

# 1234 
# 2234 
# 3334 
# 4444

for i in range(1,5):
    for j in range(1,5):
        if j <=i :
            print(i, end='')
        else:
            print(j, end='')
    print(" ")

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *
x ="*"
for i in range(1,6):
    for j in range(6,0,-1):
        if j > i:
            print(" ", end =' ')
        else:
            print(x, end=' ')
    print(" ")
# *
# * *
# * * *
# * * * *
# * * * * *
x ="*"
for i in range(1,6):
    for j in range(1,6):
        if j > i:
            print(" ", end =' ')
        else:
            print(x, end=' ')
    print(" ")

