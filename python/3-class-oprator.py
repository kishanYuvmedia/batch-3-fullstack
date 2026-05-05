# a=10
# a+=10
# #a=a+10
# print(a) #20

# print(a>2) #True
# if True:
#     print("True")
# else:
#     print("False")


# if a>2:
#     if a>20:
#         print("a is greater than 20")
#     else:
#         print("a is greater than 2 but less than or equal to 20")
# else:
#     print("False")


# if a==2:
#     print("a is equal to 2")
# elif a>2:
#     print("a is greater than 2")
# else:  
#     print("a is less than 2")


marks=int(input("Enter your marks: "))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<90:
    print("Grade B")
elif marks>=70 and marks<80:
    print("Grade C")
elif marks>=60 and marks<70:
    print("Grade D")
else:
    print("Grade F")
