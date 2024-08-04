# Exercise 
for i in range (0, 4):
  print ("Hello world")

# Exercise 2
result = (99**3)*8
print(result)


#Exercise 3
#False
#True
#False
#Error
#False

# Exercise 4
computer_brand = "Lenovo"
print (f"I have a {computer_brand} computer")


# Exercise 5  
name = "Alex"
age = 30
shoe_size = 45
info = f"My name is {name} and I am {age} years old. My shoe size is {shoe_size}"
print(info)

#Exercise 6
a = 5
b = 6
if a > b :
    print("Hello World")


#Exercise 7
number = input("Please enter the number")
number = int(number)      

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Exercise 8
my_name = "Teodor"
user_name = input("What is your name? ")

if user_name == my_name:
  print("Wow, we have the same name! That's so cool!")
else:
  print(f"Your name is {user_name}? That's a nice name, but it's no {my_name}!")

height = input ("How tall are you? ")
height = int(height)
if height >= 145:
   print ("You are tall enough to ride")
else:
   print ("You are not tall enough to ride")