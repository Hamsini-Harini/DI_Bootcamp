input = int(input("Enter a number between 1 and 100: "))
if input % 3 == 0 and input % 5 == 0:
  print("FizzBuzz")
elif input % 3 == 0:
  print("Fizz")
elif input % 5 == 0:
  print("Buzz")
