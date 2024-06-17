# Task 2
# You are required to create a stop watch that displays the elapsed time in the 
# format MM:SS that stops after a certain condition is met (say when the count reaches 100).

# inp = int(input("Enter Counter Input:"))
# counter = 0
# for i in range(inp,0,-1):
#     counter +=1
#     if i != 100:
#         print("Time Format:", i,counter)

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

''' consumers <100 
LT(1) A Category

0-50 units = 1.95
51-100 units = 3.1

consumers >100 and <200
LT(1) B Category

first 100 * 3.4
remain units * 4.8

consumes >800 
LT(1) C Category

first 200 * 5.1
201 to 300 * 7.7
301 to 400 * 9
401 to 800 *9.5
801 to remain * 10
'''

def consumption01(consumption_units):
    if consumption_units <= 100:
        print("Total Consumption Units:", consumption_units)
        if consumption_units <= 50:
            charges = (consumption_units*1.95)
            print("Charges=", charges)
        elif consumption_units >50:
            fifty_units_charge = (50*1.95)
            balance_units = (consumption_units-50)
            charges = (balance_units*3.1) + fifty_units_charge
            print("Charges=", charges)

def consumption02(consumption_units):
    if (consumption_units>100 and consumption_units<=800):
        print("Total Consumption Units:", consumption_units)
        hundred_units_charge = (100*3.4)
        balance_units = (consumption_units-100)
        charges = (balance_units*4.8) + hundred_units_charge
        print("Charges=", charges)

def consumption03(consumption_units):
    if (consumption_units>800):
        print("Total Consumption Units:", consumption_units)
        two_hundred_units_charge = (200*5.1)
        two_hundred_three_units_charge = (100*7.7)
        three_hundred_four_units_charge = (100*9)
        four_hundred_eight_units_charge = (400*9.5)
        balance_units = (consumption_units-800)
        charges = (balance_units*10) + two_hundred_units_charge+two_hundred_three_units_charge+three_hundred_four_units_charge+four_hundred_eight_units_charge
        print("Toal Charges=", charges)


no_units = float(input("Enter No of Units:"))

def power_charges(no_units):

    if no_units <=100:
        consumption01(no_units)
    
    if (no_units>100 and no_units<=800):
        consumption02(no_units)

    if (no_units>800):
        consumption03(no_units)

power_charges(no_units)