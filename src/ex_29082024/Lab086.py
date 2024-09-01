squares=[1,4,9,16,25]
#squares=[1,4,9,16,25,"chandini"]
#print(squares.sort(reverse=True))
#print(squares)

#pop-remove and return the item at index(default is last)
print(squares.pop())
print(squares)

#list is mutable in nature--it means it can change we can the change the value of index
squares[3]=64
print(squares)

#tuple-collection of items--values cannot be reassigned imutable in nature
my_tuple=(1,4,9,16,25)
print(my_tuple)

shopping_list_wife=["Bread","butter","milk","paneer"]
shopping_list_wife[1]="grains"
print(shopping_list_wife)

#real world project
#if our list is changing we use tuple if its not changing we use tuple

my_tuple=("tta.com","sdet.live")
print(my_tuple)
#converting tuple to list
my_api_list=list(my_tuple)
print(my_api_list)
my_api_list=tuple(my_api_list)
print(my_api_list)

#list is more memory but tuple uses less memory
#list has dynamic data and tuple has dynamic data

API_URLS=("https://courses.thetestingacademy.com/courses/4x-job-ready-python-automation-blueprint-selenium-api-automation/contents/66d017db691fd","https://sdet.club/t/pyatb4x-only")
print(API_URLS[0])
print(API_URLS[1])