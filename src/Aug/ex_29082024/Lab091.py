t=("The testing academy","for","The testing academy")
print(t)
print(set(t))

set1={1,2,3}
set2={4,5,6}
my_set=set1.union(set2)
print(my_set)

set1={1,3,4,5,8,9}
set2={1,2,4,5,6,9}
my_set=set1.intersection(set2)
print(my_set)

my_set=set1.difference(set2) #remove the duplicate element of S2
my_set=set2.difference(set1) #remove the duplicate element of S1
print(my_set)

set1={1,2,3,4,5}
set2={2,3,4}
my_set= set2.issubset(set1)
print(my_set)