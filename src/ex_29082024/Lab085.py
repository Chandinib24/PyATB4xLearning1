#List -collection of items(duplicates re allowed)
# different types of data can be stored in a single list

my_list=[1,2,3]
#my_list 2=[1,2,"chandini"]

print(my_list)
print(len(my_list)) #length always strats from 1 wherein index starts from 0

print(my_list[0])
print(my_list[1])
print(my_list[2])
# print(my_list[10]) #list index pout of range exception
my_list[0]="Pramod"
my_list[1]="Science"
my_list[2]="24"

print("elemet at the index 0-",my_list[0])
print("elemet at the index 0-",my_list[1])
print("elemet at the index 0-",my_list[2])

print(my_list)
for element in my_list:
        print(element)


print("-----------------------")

my_list=[1,2,3]

#Append
my_list.append(4)
my_list.append(5)#Add the objetc at the end of the list
print(my_list)#append can take multiple arguments


#extend -to add one or more elements we use extend nd also we can add different data types
my_list.extend([10,20,30])
my_list.extend([40])
my_list.extend(["chandini"])
print(my_list)

#inser()--where we need to add elements shifted insert a object before index
my_list.insert(2,"Basavaraju")
print(my_list)
print(len(my_list))

#To rep;ae he value just reassign
my_list[1]="B"

my_list.insert(0,0)
print(my_list)
my_list.insert(-1,"science")
print(my_list)

#remove
my_list.remove("B")
print(my_list)

print("-----------------------------")

my_copy_list=my_list.copy()
print(my_list)
print(my_copy_list)

my_list.clear()
print(my_list)
print(my_copy_list)

my_copy_list.remove("B")
# my_copy_list.remove("chandini")
# my_copy_list.remove("Basavaraju")
# my_copy_list.remove("science")
#my_copy_list.sort()
print(my_copy_list)

my_copy_list.reverse()
print(my_copy_list)