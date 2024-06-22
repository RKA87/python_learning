# Task 1
# Write a program to calculate the average height of a group of persons given as 20, 30, 42,2,45,56,89,31 using *args as part of the function. 

def avg_height(**kwargs):

    # height=2.54
    avg_height= (kwargs)
    print("Average Height:", avg_height)

avg_height(man1="20", man2="30", man3="42", man4="2", man5="45",man6="56", man7="89", man8="31")

def height(*args):
    for x in args:
        height=float(2.54*x)
        print("Average Height:", height)

height(20, 30, 42,2,45,56,89,31)
'''
Task 2
Write a program to display the total count of Oranges in the following shopping cart using **kwargs.

Cart = {
“Oranges” : 20,
“Apples” : 30,
“Pears” : 21,
“Oranges” : 30,
“Mangoes” : 40,
“Berries” : 20,
“Oranges” : 60
}
'''

