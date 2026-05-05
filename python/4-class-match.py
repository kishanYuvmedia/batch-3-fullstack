age=int(input("Enter your age: "))
match age:
    case 5:
        name=input("Enter your name: ")
        print(f"Hello {name}, you are 5 years old")
        print("You are 5 years old")
    case 10:
        print("You are 10 years old")
    case _:
        print("You are not 5 or 10 years old")