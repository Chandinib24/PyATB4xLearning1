my_shopping_list=["Bread","milk","butter"]
print(my_shopping_list[0])
print(len(my_shopping_list))

def bring_more_food(my_list):
    more_tem=input("Enter the item \n")
    my_list.append(more_tem)#my_list.append("cheese")
    my_list.insert(0,more_tem) # insert is for positional input
    return my_list

l=bring_more_food(my_shopping_list)
print(l)

#set is a function to remove the duplucates from list