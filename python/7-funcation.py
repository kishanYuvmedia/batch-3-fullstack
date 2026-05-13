# with peramiter without return type
def sum(a,b):
    print(a+b)
sum(20,40)

# with peramiter with return type
def sum(a,b):
    return a+b

result=sum(20,40)
print(result)

# without peramiter with return type
def greet():
    return "Hello, World!"
message=greet()
print(message)

# without peramiter without return type
def greet():
    print("Hello, World!")

greet()


age= lambda x: x+10
print(age(20))