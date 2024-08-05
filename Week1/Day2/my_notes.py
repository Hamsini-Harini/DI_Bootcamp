#first way to do it - manual
list = [5, 10, 15, 20, 25, 50, 20]
list [3] = 200
print(list)

#second way to do it
list = [5, 10, 15, 20, 25, 50, 20]
find_index = list.index(20)
list[find_index] = 200
print(list)

#if I want to replace all occurances of 20, no funciton for that so we need a while loop

# Task from platform inside Day 2 - loops- make multiplication list of a number

number = 5
multi_list = range(0, 6)
for number in multi_list:
    print(number * 5)
