# first basic function
# receives number, adds 2, prints result

# this is the users input
num1 = float(input("Please Enter A Number"))
# this is where the input is processed
total = num1+2
# this is the output result
print("Your Number Is:", total)

# second basic function
# receives number x, calc y=3*x+2 prints y

# this is the users input
y = float(input("Please Enter A Number"))
# this is where the input is processed
total = 3*y + 2
# the output result is then generated
print("Your Number Is:", total)

# third basic function
# receives number, creates loop, counts up to number but does not include, prints result

# user input
number = int(input("Please Enter Your Number"))
# the loop is created, input is processed
for x in range(number)
# the output is then generated
print(x)

# fourth basic function 
# receives number, creates loop using n, enters values into list [], prints list

# method 1: required number of inputs to begin with
# users input of how many items in the users list
n = int(input("How Many Items Are In Your List:"))
# 'list1 = {}' is the creation of an empty list
list1 = []
for i in range(n):
# the users second input, the list elements
element = input("Enter The Element:")
list1.append(element)
# output list is printed
print("Your List:",list1)

# method 2: user is asked if another input is wanted
# 'list1 = []' is the creation of an emoty list
list1 = []
while True:
# users input
element = input("Enter The Element:")
choice = input("Want To Stop? If Yes Type 'yes' If Not Press Any Other Key!")
if choice == "yes":
# 'break' discontinues the user inputs
break
# output list is printed
print("List Of Elements Are:",list1)

# method 3: allows for input of letters, integers and decimals
import ast
# 'list1 = []' is the creation of an emoty list
list1 = []
while True:
# user input
# using 'ast.literal_eval' it allows for the input of letters and decimals
element = ast.literal_eval(input("Enter The Element:"))
list1.append(element)
# if user has no more inputs, 'yes', will generate the list
choice = input("Want To Stop? If Yes Type 'yes' If Not Press Any Other Key!")
if choice == "yes":
# 'break' discontinues the user inputs
break
# output list is printed
print("List Of Elements Are:",list1)

# method 4: printed list when written with spaces such as: 1 2 3 4
# there is no need to create an empty list as they inputed at once
# user input
n = input("Enter Elements With Spaces")
list1 = n.split()
# output printed
print(list1)








