#order Dic
#dictionary that remembers the insert ordeer

from collections import OrderedDict

d=dict()#Normal dictionary order not maintained
d["age"]=78
d["name"]="Praomod"
d["address"]="ABC"
d["ID"]="123"
#Since its a small example now it will be displayed in order
print(d)

od=OrderedDict()#Maintains the order
od["Bananna"]=1
od["carrot"]=2
od["raddish"]=3
print(od)