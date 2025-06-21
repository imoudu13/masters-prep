""" 
1. Variables
2. Data types
3. arithmetic
4. lists/arrays
5. functions
6. if statements
7. loops (while, for)
8. input
"""

# snake case variable naming
my_girlfriend = "Daniella"

# number
num = 10
# string
string = "hehe"

# lists
# you can put multiple data types in lists in python
arr = [10, "lemon", [15, 5]] # [number, string, list]

# how to define functions
# def function_name(param1, param2, param3):
    # code
def moella(x, y, z):
    print(x * y + z)

# how to call the function
moella(1, 2, 3)

x = 10

# if statement
if x < 15:
    print("Less than 25")
    x += 10
elif x > 25:
    print("Greater than 25")
else:
    print("Done")
    

"""
There are two ways to use for loops in Python.
Use the range function for when you have a set amount of times you want to iterate.
Or you can iterate through an iterable object (usually a list).
"""

"""
For the range function the first number is the number you are starting at
the second is the one you want to stop at, it will stop before it.
so in this case it will start at 0, and go until 24
you can also add another number for the amount you want to increase
range(0, 25, 5) will start at 0, stop at 24, and increase by 5 on each iteration)    
"""

# range function
for i in range(0, 25): # range(inclusive, exclusive, skip_amount)
    print("Hello World!")


array = [1, 34, 34, 65, 23, 7, 8, 23, 87, 98, 12]


"""
This one iterates through every element in the array, starting at the first. 
It's a for each loop. This for loop iterates through each element and prints it.
"""
for arr in array:
    print(arr)


y = 16

"""
While loops
"""
while y < 100:
    y += 1


"""Input"""
# To accept user input, you can use the input function like so:
name = input("Enter your name: ")
age = input("Enter your age: ")

# it will wait for you to type something and hit enter. the value will be saved as a string
# if you need to do math with it you can change it to an number using the int() function
age = int(age)

print("Hello,", name, ". You are", age, "years old")