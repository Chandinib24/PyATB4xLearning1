#Dict
#key and value
#name=chandini

student_info1={
      "name":"chandini",
      "age":26,
      "age":27,
      "address":{
            "home_address": "New delhi",
            "office_address": "KA"
      }
      }

student_info2={
      "name":"Sushma",
      "age":35,
      "address":{
            "home_address": "Bangalore",
            "office_address": "Mysore"
      }
      }

student_list=[student_info1,student_info2]
print(student_list)

print(student_info1)
print(student_info1["name"])
print(student_info1["age"])
print(student_info1["address"])


student_info1["age"]=50
print(student_info1)


student_info=dict( name="chandini",ge=26,age=27,address="KA")
#dictionary is a unordered collection of data
