#Task 1 - The Corporation has listed the requirement for shortlisting the candidates for a worker’s job. The conditions are as under:
# Applicant should be male
# Applicants should be between 20 and 25 years of age.
# Applicants should have been born after 2024 January 1

# If the applicant meets the above condition, display the message “Shortlisted”. Else display “Not Shortlisted”

# Accept the details of gender (M/F), age (in years) and date or birth (dd/mm/yyyy) from the user.

applicant_gender=input('Enter applicant gender:')
applicant_age = int(input('Enter applicant age:'))
applicant_dob = (input('Enter applicant dob in dd/mm/yyyy format:'))

x = applicant_dob.split("/")

applicant_dob = int(x[2])

if (applicant_gender == "M" and (applicant_age >= 20 and applicant_age <=25) and (applicant_dob >= 2024)):
    print("candidate shortlisted")
else:
    print("candidate not shortlisted")

#Task 2 - Eligiblie for Position of Receptionist
# Applicant should #Tnot be married, 
# should be Female, 
# should be less than 30 years age and should not have more than 1 years experience, 


Age = input("Enter Applicant Age:")
Applicant_Age = int(Age)
Applicant_Gender = input("Enter Applicant Gender:")
Applicant_MaritalStatus = input("Enter Applicant Marital Status:")
Experience = input("Enter Applicant Experience:")
Applicant_Experience = int(Experience)
#case1 (Nested IF's will based on True statement execution)
if Applicant_Age <30:
    if Applicant_Gender =="Female":
        if Applicant_MaritalStatus == "Single":
            if Applicant_Experience <1:
                print("Applicant Eligible for Receiptionist Position")
            else:
                print("Application not suitable for requirement position")

#case2
if (Applicant_Age < 30 and Applicant_Gender == "Female" and Applicant_MaritalStatus == "Single" and Applicant_Experience < 1 ):
    print("Applicant Eligible for Receiptionist Position")
else:
    print("Application not suitable for requirement position")

#Task 3 - Planning to give hike in salaries to its employees
# if Employee is Manager the hike is 10% 
# if Employee is not Manager the hike is 20%,
# Calculate Hike
# Display New Salary Hike 

#case 1
Employee_Designation = input("Enter the Designation of Employee: ")
Actual_Salary = float(input("Enter Your Salary:"))

if Employee_Designation == "Manager":
    Percentage_Output = float(Actual_Salary*10/100)
    New_Salary_After_Hike = Actual_Salary+Percentage_Output
    print("New_Salary_After_Hike:", New_Salary_After_Hike)
else:
    Percentage_Output = float(Actual_Salary*20/100)
    New_Salary_After_Hike = Actual_Salary+Percentage_Output
    print("New_Salary_After_Hike", New_Salary_After_Hike)

#case 2 #using ternary operator
New_Salary_After_Hike=Actual_Salary+float(Actual_Salary*10/100) if Employee_Designation == "Manager" else Actual_Salary+float(Actual_Salary*20/100)
print("New_Salary_After_Hike:", New_Salary_After_Hike)

#Task 4:
#Create a new string made of the first, middle, and last characters of each input string

str1=input("Enter String:")
tot = int(len(str1)/2)

print("First Character:", str1[0])
print("Middle Character:", str1[tot])
print("Last Character", str1[-1])

print("New String:", str1[0]+str1[tot]+str1[-1])

#Task 5: Reverse a given string
str = "RAM"
length = len(str)-1

new_string = ""

for i in range(length, -1, -1):
    new_string +=str[i]

print("Reversed String:", new_string)

#Task 6 Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, 
# Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result



# Task 7:
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1

s1=input("Enter First String:")
s2=input("Enter Second String:")

#case1
sl_len =int(len(s1)/2)
s3=s1[:sl_len] + s2 + s1[sl_len:]
print(s3)

#case2
len=len(s1)
fi = ""

for i in range(0,sl_len):
    fi += s1[i]

second_stage=fi+s2

for i in range(sl_len,len):
    second_stage +=s1[i]

print(second_stage)

#Task 8 A bank will offer a customer a loan if they are 18 or over and have an annual  income of at least Rs. 35000. 
# Write a program that will, based on a customers age and income, produce a decision on whether they will be offered a loan.

customer_age = int(input("Enter Customer Age:"))

customer_income = float(input("Enter Customer Income:"))

if (customer_age >= 18) and (customer_income >= 35000):
    print("loan can be offered from bank")
else:
    print("Bank Requirements not met")

#Task 9 
'''
To enroll on an online course a prospective student has to be at least 21 and have passed their qualifying examination. The user will be asked the following questions:

How old are you?
Have you passed your qualifying examination (Y/N)?

In response to the questions the program will display one of the strings shown below:.

You can enroll in the course.
You cannot enroll in the course. 
'''
#case1
student_age = int(input("How old are you:"))
exam_result = input("Have you passed your qualifying examination (Y/N)?")

if (student_age >= 21) and (exam_result == "Y"):
    print("You can enroll in the course")
else:
    print("You cannot enroll in the course")

#case2
print("You can enroll in the course") if (student_age >= 21) and (exam_result == "Y") else print("You cannot enroll in the course")