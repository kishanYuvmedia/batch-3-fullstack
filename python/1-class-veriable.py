
name='John Doe'
age=30
print(type(name)) #str
print(type(age)) #int
global city
city=["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
#we can access the global variable city in this function
print(type(city)) #list
state=("California", "Texas", "Florida", "New York", "Illinois")
print(type(state)) #tuple
country={"USA": "United States of America", "CAN": "Canada", "MEX": "Mexico"}
print(type(country)) #dict
is_student=True
print(type(is_student)) #bool
subjects={"Math", "Science", "History","History", "English", "Art"}
print(type(subjects)) #set

print("Name:", name)
print("Age:", age)
print("City:", city)
print("State:", state)
print("Country:", country)
print("Is Student:", is_student)
print("Subjects:", subjects)
print(city[0]) #New York
print(state[1]) #Texas
print(country["USA"]) #United States of America
print(subjects) #order is not guaranteed in a set  
print(city[0:4]) #['New York', 'Los Angeles', 'Chicago', 'Houston']
print(state[0:3]) #('California', 'Texas', 'Florida')