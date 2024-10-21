a,b,c=(10,11,12)

print(a)
print(b)
print(c)

#sarch in tuple
cities=("Lodon","paris","tolyo","New Delhi")
print("paris" in cities)
print("France" in cities)

t=(12,34,56)
#t.append(12)#'tuple' object has no attribute 'append'
my_list=list(t)
my_list.append(80)
t=tuple(my_list)
print(t)