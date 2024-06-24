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
#SyntaxError: keyword argument repeated: Oranges

#duplicate keys finding 
raw_dict = {
    "Apples": 80,
    "Mangoes": 30,
    "Oranges": 80,
    "Grapes": 50,
    "Banana": 60,
    "Oranges": 60,
    "Apples": 20
    }

res = {}

for key,val in raw_dict.items():
    if key not in res:
        res[key]=val
        print(res)
'''
Task 3:

Write a program to calculate the fare for each station from the given data.
Fare is calculated using the formulate distance * cost. 
The cost is given in an an array like so 200, 350, 55, 724, 120
The distance for each station is given in the dictionary below
{
“Delhi” : 650,
“Kolkata” : 700,
“Mumbai” : 625,
“Chennai” : 400,
“Pune” : 600
}

Use *args and **kwargs as function parameters
'''
def fare_cost(*args, **kwargs):

    cost_list=[]
    for arg in args:
        cost_list.append(arg)
    
    print("cost list:", cost_list)
    distance=kwargs
    
    empty_list = []

    for val in distance.values():
        print(val)
        empty_list.append(val)
    
    distance_cost_result=[]

    for i in range(0,len(cost_list)):
        x= empty_list[i]*cost_list[i]
        distance_cost_result.append(x)
    
    print(distance_cost_result)

    x=[]
    for key in distance.keys():
        x.append(key)

    final_result_dictionary={}
    for i in range(len(x)):
        final_result_dictionary[x[i]]=distance_cost_result[i]

    for key in final_result_dictionary.keys():
        print("Cost of", key ,"=", final_result_dictionary[key])

cost_list = [200,350,55,724,120]

fare_cost(*cost_list,Delhi= 650,Kolkata=700,Mumbai= 625,Chennai= 400,Pune=600)

'''
The following information is provided to you. You need to write a program to create an Address Slip.

First Name : John 
Middle Name : Bruce
Last Name : Mayers

Address: 
Street:  2155 Buffalo Creek Road
City:  Nashville
State/province/area:   Tennessee
Phone number:  615-833-5442
Zip code:  37211
Country calling code:  +1
Country:  United States

Items: 
Pens - 10, Books - 23, Pencils - 15, Erasers - 25

You are given the items in an array, the address as a dictionary and the first name, last name and middle names as individual variables. 
The address slip should print the First Name + Middle name + Last Name followed by the address and the total number of items. 

'''

def address_slip(f_name,m_name,l_name,*args,**kwargs):

    First_Name = f_name
    Middle_Name = m_name
    Last_Name = l_name
    data = kwargs

    print("FirstName:{} \nMiddleName:{} \nLastName:{}".format(First_Name, Middle_Name, Last_Name))

    Items=[]
    for arg in args:
        Items.append(arg)
    
    items_details = ["Pens", "Books", "Pencils", "Erasers"]
    print('\n'"Items List follows below:")
    for i in range(len(items_details)):
        print("{} - {}". format(items_details[i], Items[i]))
    
    print('\n'"Address Slip:")

    for key,val in data.items():
        print(key, ":", val)

list_array = [10,23,15,25]
address_slip("Rakesh", "Kumar", "Akuluru",*list_array, Street = "2155 Buffalo Creek Road", City = "Nashville", State = "Tennessee", PhoneNumber = "615-833-5442", 
             Zipcode="37211", CallingCode = "+1", Country = "UnitedStates")

'''
Task 6

Write a program to print the cost of each item from the following.  

Units = 5, 20, 11, 23, 51, 85, 90
Price = 200, 10, 11, 230, 10, 10, 9

The cost of each item is calculated using the formula Price / units.
'''

def each_item_cost(list1,list2):
    
    units_list = list1
    prices_list = list2

    print("Units List:", units_list)
    print("Prices List:", prices_list)

    for i in range(0,len(prices_list)):
        print("Cost of Each Item:", prices_list[i]/units_list[i])


first_list = [5, 20, 11, 23, 51, 85, 90]
second_list = [200, 10, 11, 230, 10, 10, 9]

each_item_cost(first_list, second_list)
'''
Task 7

Write a table to display the squares of the numbers given as *args

2,4,10, 7, 23, 45, 11

'''

def table(*args):

    x=[]
    for arg in args:
        x.append(arg)
    
    print("list:", x)
    for each_num in x:
        for i in range(1,11):
            print(arg,"x", i, "=", arg*i)
        print("+++++++++++++++++++")


table_list = [2,4,10, 7, 23, 45, 11]
table(*table_list)

'''
You are given the details of books in the following array. Write a program to print the Author’s Name.
'''
def authors_name(books):
    
    list = books
    for i in range(0,len(list)):
        x=books[i]
        print("Author's Name:", x['author'])


books = [
    { 
        "title" : "Do Android Dream of Electric Sheep",
        "author" : "Philip K. Dick"
    },
    { 
        "title" : "Something wicked this way comes",
        "author" : "Ray Bradbury"
    },
    { 
        "title" : "The curious incident of the dog in the night time",
        "author" : "Mark Hadden"
    },
    { 
        "title" : "The Story of Yesterday",
        "author" : "Sergio Cobo"
    },
    { 
        "title" : "To kill a Mocking bird",
        "author" : "Harper Lee"
    }
]

authors_name(books)
'''
Task 9
Write a program to calculate the sum of a list of numbers using recursion.
'''

def addition(n):

    if n==0:
        return 0
    else:
        z = n + addition(n-1)
        return z

x=addition(5)
print(x)

#case 2
sum=0
i=0
for i in range(100+1):
    sum += i
    print(sum)

#case 3
while i<=100:
    sum=sum+i
    print(sum)
    i+=1
    print(i)
'''
Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.
Test Data :
(power(3,4) -> 81
    
'''
def power_output(int1,int2):
    input1=int1
    input2=int2

    result = 1
    for i in range(input2):
        result = result*input1

    return result

#case 2
def power(x,y):

    if y==0:
        return 1
    else:
        z = x * power(x,y-1)
        return z

x=power(4,5)
print(x)
