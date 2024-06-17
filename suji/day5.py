age = input("Enter your age")
gender = input("Enter your gender as M or F")
DOB = input("enter DOB in dd/mm/yyyy format")
age =int(age)
date= DOB.split("/")
print(date[0],date[1],date[2])
if date[1] == "1" or date[1]=="3" or date[1]=='5'or date[1]=='7' or date[1]== '8' or date[1] == '10' or date[1]== '12':
    month=31 
elif date[1] == '2' :
    month=28
else :
    month=30
   #print(type) 
DOB_final = (date[2]*1000 + date[1]*month +date[0])  
print(DOB_final)         
'''if gender== 'M' and 25>age>20 and DOB_final>2024001 :
    print("shortlisted")
else:   
    print("Not shortlisted")'''