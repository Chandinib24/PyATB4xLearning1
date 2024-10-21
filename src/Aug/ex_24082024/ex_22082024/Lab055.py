#Match statement
#switch in Java
#match the op ad execute
#python >3.10


#Match variable:
#case pattern 1:
#code block
#case pattern 2:
# code block

#write a program to ask the user in which browser to run the automation
Browser_name=input("Enter the name of the browser \n")
Browser_name=Browser_name.lower()
match Browser_name:
    case "chrome":
        if Browser_name=="chrome":
            print("Heello")
        print("Execute the chrome code")
    case "safari":
        print("Execute the safari code")
    case "firefox":
        print("Execute the firefox code")
    case _:
        print("Browser not found")





