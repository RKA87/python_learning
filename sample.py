# Task 2
# You are required to create a stop watch that displays the elapsed time in the 
# format MM:SS that stops after a certain condition is met (say when the count reaches 100).

# inp = int(input("Enter Counter Input:"))
# counter = 0
# for i in range(inp,0,-1):
#     counter +=1
#     if i != 100:
#         print("Time Format:", i,counter)

# kilometer_cost = 15

# journey_time_hours = int(input("Enter the total journey time which include break covers during travel:"))

# total_kilometers = int(input("Enter total kilometers:"))

# if journey_time_hours < 2:
#     trip_charges = kilometer_cost*journey_time_hours
#     print("Total Kilometers:", total_kilometers)
#     print("Journey Time Duration:", journey_time_hours)
#     print("Total Trip Charges:", trip_charges)

# if journey_time_hours>=2:

#     waiting_charge = 5
#     waiting_charge_input = int(input("Enter Waiting Charge in Minutes:"))
#     total_Waiting_charges = (waiting_charge_input*5)

    


#     break_charges = 5
#     break_charge_input = int(input("Enter break charges in mts:"))
#     total_break_charges = (break_charges*break_charge_input)

x=[]
# for i in range(2,11,2):
#     x.append(i)

# print(len(x)-1)

# for i in range(2,10,2):
#     x.append(i)
# print(len(x))

# tot_journey = 0
# brk = 0.5
# count = 0
# for i in range(2,13,2):
#     tot_journey = tot_journey + 2 + brk
#     print(tot_journey)
#     if tot_journey < 13:
#         count +=1
#         print(count)

# Write a program to display the total count of Oranges in the following shopping cart using **kwargs.

# Cart = {
# “Oranges” : 20,
# “Apples” : 30,
# “Pears” : 21,
# “Oranges” : 30,
# “Mangoes” : 40,
# “Berries” : 20,
# “Oranges” : 60
# }

# def count_of_oranges(**kwargs):

#     cart = kwargs

#     for x in cart:

cart = {
    "Apples" : 30, 
    "Pears" : 21, 
    "Oranges" : 30, 
    "Mangoes" : 40, 
    "Berries" : 20, 
    "Oranges" : 60
    }

print(cart["Apples"])
print(cart.get("Apples"))
x=(cart.items())

for x,y in cart.items():
    print(x,y)