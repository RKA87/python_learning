#print("helloworld")

var1 = 'C:\suji\path'
print ('var1=', var1)
#print('C:\suji\path')

var2= r'It\'s a holiday'
print(var2)

a=10
print(type(a))


name = "pythpon"

print(name[0])

print(name.replace("p" , "J"))

text = "hello\njohn"
o = (text.split(" "))
print(o)


o1 = (text.split("\n"))
print(o1)

print("\n".join(o1))

print(f'checking the output= {o1} \n', name, "coming up in new line") 

str1="Sujana"
print(str1[0]+str1[2]+str1[4])

print("InputString=", str1)

#first letter
print(str1[0])

#second letter to print j
l = int(len(str1)/2)

print(type(str1[l]))
x=str(str1[l-1])

y=(str1[0]+x)

#3rd letter

print(y+str1[-2])

count = 10_1234_567_8910
print(count)


print(bool('100'))

test = "JaSonAy"

mi = (len(test)/2)
print(float(mi))


# outp=test[mi-1:mi+2] #2:5
# print(outp)
