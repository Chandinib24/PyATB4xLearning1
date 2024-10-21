user_type=input("Enter the user type admin,guest,manager \n")
user_type=user_type.lower()

match user_type:
    case "admin" | "manager":
        print("Hello sir")
    case "guest":
        print("Hello guest")
    case _:
        print("Not found")