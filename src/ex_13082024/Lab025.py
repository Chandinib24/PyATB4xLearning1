name="ChandiniB"

print(type(name))
print(name.upper())
print(name.lower())
print(len(name))

a="90"
print(type(a))#anything is in double quotes and single  is string

b=(78)
print(type(b))

name="This is a big line"
print(type(name))
name= name + str(1) # we cannot add stringa nd integer , so we can put 1 in doble quotes or we can convert to string
# so concatenation will happen
print(name)


first_name="Chandini"
last_name="Basavaraju"
full_name=first_name+last_name
print(full_name) #concatination

how_many_planes_i_have=None
print(type(how_many_planes_i_have))#None type
#null is not there in python

value=0 #This is int

#id- returns the identity of the object

age=10
age2=10
print(id(age))
print(id(age2)) #these are the place/memory where the object is stored is called id , same id because two values are same hence memory can be saved

height=6.5
height1=7.5
print(id(height))
print(id(height1)) #id's are diff because values are different
