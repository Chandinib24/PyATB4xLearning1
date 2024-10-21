# 1. Explain the difference between the = operator and the == operator in Python.
#Answer--->
# In python = operator is also called as assignment operator which is used to assign the value to the
# to the right hand side
#  example x=20 , name='chandini'

#== operator->in python this is called as comparison operator wherein it compares the value present in
# left hand side to the value present in right hand side and returns the result in Boolean form
#Example
x=10
y=5
print(x==y)# output is false 

# What does the ** operator do in Python, and how is it used?
#Answer--->
#** operator in python is used to calculate the power of the base value
#example 2**3 , here 2 is base and 3 is the exponent
print(2**3) #output is 8

# What does the ^ operator do in Python, and in what context is it commonly used?
#Answer--->
# In Python, the ^ operator is the bitwise XOR (exclusive OR) operator.
#
# The ^ operator compares each bit of two integers. For each bit position:
# The result bit is 1 if the corresponding bits of the operands are different
# (one is 1 and the other is 0).
# The result bit is 0 if the corresponding bits are the same (both 0 or both 1).
a = 12   # binary: 1100
b = 7    # binary: 0111
result = a ^ b  # binary: 1011, which is 11 in decimal
print(result)   # Output: 11


