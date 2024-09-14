##try,except and Finally
#file

import os

# file=open('example.txt','r')#FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'
# print(file.read())

try:
    full_path=os.getcwd()
    print(full_path)
    full_path_file=full_path+"/example.txt"
    file=open(full_path_file,'r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("File not found,Fix the path and crate a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)
