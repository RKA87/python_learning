#1st Task
var1= 30
var2= 10

#case 1
print ("The Order is:")
print ("Apples:", var1)
print ("Oranges:", var2)
print ("Total:", var1+var2, "Units")
#case 2
print (f"The Order is listed below: \nApples:{var1} \nOranges:{var2} \nTotal:{var1+var2} Units")
#case 3
print(f"The Order is listed below: \nApples:{var1} \nOranges:{var2} \nTotal:{var1+var2} Units".format(var1, var2))

#2nd case
test_string = 'The Order is:  \
Apples: 30 \
Oranges : 10 \
Total : 40 Units \
'
print (test_string)

#3rd case
print ("The Order is: \nApples: 30 \nOranges : 10\nTotal : 40 Units")

#4th case
test_string = '''
The Order is:  
Apples: 30
Oranges : 10
Total : 40 Units
'''
print (test_string)


#2nd Task
#In the string "Hello world" print the following output - "world hello"

x = "Hello world"

output = x.split(" ")

print(type(output))
print("Final Output=", output[1]+output[0])

#In the string "Hello world" print the following - "Hd" "el"
#case 1
output1=(x.split('ello worl'))
print(output1[0]+output1[1])

output2=(x.lstrip("H"))
print(output2[0]+output2[1])


#case2
print(x[0]+x[-1] )
print(x[1:3])

#Task 3
#In the string "Hello world" for the 2 words Hello and World get the length separately and print the difference of the lengths
print ("Total_Length=",len(x))
print ("First Word Length=", len(x[0:5]))
print ("Second Word Length=", len(x[6:]))
print ("Difference of the Length=", len(x[0:5])-len(x[6:]))