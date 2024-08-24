# write  a python program to calculate the area of circle givem its radius using the formula
# Area= pi*r power 2 take pie as 3.14
import math

#Logic building formula
# Step 1 -- figure out the input and ourtput
#input-r-data type-float
#pi->3.14
# power--> pow or ** --any

# o\p -foat with area

#Step 2
# rough logic area
# #step 3 write the logicow(radius,2)

radius= float(input("Enter the radius of circle"))
print(radius)
print(math.pi)
area=math.pi*math.pow(radius,2)
area2= 3.14*(radius**2)
print("Area of circle is", area)
print(f"Area of circle is {area:.2f}")
print(area2)

#* --multiplication
#**- power