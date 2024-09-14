#deque-double nded que
#FIFO- bus stand que, airport que
#A list like sequence optimized for data accesses near endpoints

from collections import deque

#create a deque
#d=deque()
d=deque([1,2,3])
print(d)

d.append(4)#item
print(d)

#add an element o left end
d.appendleft(0)
print(d)

#extend the deque from left with an iterable
d.extend([5])
print(d)