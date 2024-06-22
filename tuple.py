thistuple = ("apple", "banana", "cherry")

print(thistuple)
print(type(thistuple))

#duplicate items allowed in tuple
thistuple1 = ("apple", "banana", "cherry", "apple", "cherry", 34, True)

print(type(thistuple1))

#create a tuple with only one item, must require to add a comma
ex = ("abc",)

print(type(ex))

print(thistuple1[-1])

#Return the third, fourth, and fifth item:
thistuple2 = ("apple","banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple2[2:5])

#Negative Indexing
print(thistuple2[-4:-1]) #returns the items from index -4 (included) to index -1 (excluded)

#using IN operator

if "apple" in thistuple2:
    print("Yes")
else:
    print("Not Match")


#add item into tuple
thistuple2 = ("apple","banana", "cherry", "orange", "kiwi", "Rakesh","melon", "mango")

new_list = list(thistuple2)
new_list.insert(3, "Rakesh")
new_list.append("Suji")
print(new_list)
new_tuple = tuple(new_list)
print(new_tuple)
print(type(new_tuple))

#add tuple + tuple
added_tuple = thistuple2 + new_tuple
print(added_tuple)

#Remove tuple element, since it is unchangeable need to convert into list and then remove the element and convert into tuple finally
print("this tuple2:", thistuple2)
convert_in_list = list(thistuple2)
convert_in_list.remove("apple")
convert_in_tuple = tuple(convert_in_list)
print(convert_in_tuple)

for i in range(len(thistuple)):
  print(thistuple[i])

print(new_tuple.count("Rakesh"))

#get the index value by input of element "banana" from that tuple 
x=(new_tuple.index("banana"))
print(x)

fruits = {"apple", "banana", "cherry"}
fruits.remove("apple")
print(fruits)