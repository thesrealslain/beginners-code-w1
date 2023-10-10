# first: basic function 
# write a function named sayName that displays your name

def sayName():
    print("slain")

# second: basic function
# write a function named sayHello2 that uses two print statements to display the text "Hello World"

def sayHello2():
    print("Hello")
    print("World")

# third: basic function
# write a function called dollars2pounds which converts a dollar's value it pounds, use the formula: 0.80 x dollar value

def dollars2pounds():
    num1 = float(input("Enter Your Dollar Value: "))
    pounds = 0.80*num1
    print("Your Value In Pound Sterling Is:", pounds)



# fourth: basic function
# write a function called tenHellos that uses a loop to display "Hello World" ten times (on seperate lines)

def tenHellos():
    print("Hello World"\n*10)
    
# fith: basic function
# suppose the prices of train tickets are increasing by 2% every month, write a function called railFareIncrease,
# which begins by printing the current price of a ticket from Southampton to Portsmouth: £16.50, it should then display the price for 11 more months
# this is the updated method using a loop

def railFareIncrease():
    initialTicket = 16.50
    print(f"Month 1: £{initialTicket:.2f}")

    for month in range(2, 13):
        initialTicket = initialTicket*1.02
        print(f"Month {month}: £{round(initialTicket, 2)}")
railFareIncrease()

# this is the old method not using a loop
# far longer but produces the results personalised with their months

def railFareIncreases():
    num1 = 16.50*1.02
    num2 = num1*1.02
    num3 = num2*1.02
    num4 = num3*1.02
    num5 = num4*1.02
    num6 = num5*1.02
    num7 = num6*1.02
    num8 = num7*1.02
    num9 = num8*1.02
    num10 = num9*1.02
    num11 = num10*1.02
    
    print("January: £16.50")
    
    number1 = num1
    rounded_number1= format(number1,".2f")
    print("February:", rounded_number1)
    
    number2 = num2
    rounded_number2= format(number2,".2f") 
    print("March:", rounded_number2)
    
    number3 = num3
    rounded_number3= format(number3,".2f")
    print("April:", rounded_number3)
    
    number4 = num4
    rounded_number4= format(number4,".2f")
    print("May:", rounded_number4)
    
    number5 = num5
    rounded_number5= format(number5,".2f")
    print("June:", rounded_number5)
    
    number6 = num6
    rounded_number6= format(number6,".2f")
    print("July:", rounded_number6)
   
    number7 = num7
    rounded_number7= format(number7,".2f")
    print("August:", rounded_number7)
    
    number8 = num8
    rounded_number8= format(number8,".2f")
    print("September:", rounded_number9,".2f")
    
    number9 = num9
    rounded_number9= format(number9,".2f") 
    print("October:", rounded_number9)
    
    number10 = num10
    rounded_number10= format(number10,".2f")
    print("November:", rounded_number10)
    
    number11 = num11
    rounded_number11= format(number11,".2f")
    print("December:", rounded_number11)

# sixth: basic function
# write a function named countTo that asks the user for a number and count from one to that number

def countTo():
    number = int(input("Enter A Number: "))
    for x in range(number):
    print(x+1)

# seventh: basic function
# based on your solution to the previous question, write a function named countFromTo that asks the user for two numbers. The first number is the start of the count and the second one is where the count ends

def countFromTo():
    number1 = int(input("Enter Your First Number: "))
    number2 = int(input("Enter Your Second Number: "))
    for number in range(number1, number2):
        print(number+1)

# eigth: basic function
# write a function named changeCounter, this should ask the user how many 1p, 2p and 5p coins they have (using separate questions), and then display the total amount of money in pence

def changeCounter():
    number1 = int(input("How Many 1p Coins Do You Have: "))
    number2 = int(input("How Many 2p Coins Do You Have: "))
    number3 = int(input("How Many 5p Coins Do You Have: "))
    num2 = number2*2
    num3 = number3*5
    total = number1 + num2 + num3
    print("You Have A Total Of:", total,"Pence")

# ninth: harder function
# harder: write a function named weightsTable that prints a table of kilogram weights (between 10 and 50) and their ounce equivalents

# this format uses a loop to generate the values for set inputs not by a user

def weightsTable():
    number1 = float(input("Enter Your Kilogram Value: "))
    number2 = float(input("Enter Your Kilogram Value: "))
    number3 = float(input("Enter Your Kilogram Value: "))
    number4 = float(input("Enter Your Kilogram Value: "))
    number5 = float(input("Enter Your Kilogram Value: "))

    num1 = number1*35.274
    num2 = number2*35.274
    num3 = number3*35.274
    num4 = number4*35.274
    num5 = number5*35.274

    print("Kgs  |  Ounces")
    print("==============")
    print(number1,  "|",  num1)
    print(number2,  "|",  num2)
    print(number3,  "|",  num3)
    print(number4,  "|",  num4)
    print(number5,  "|",  num5)

# this format uses a loop to convert values already inputted, rather than inputs from a user

def weightsTable():
    print(" Kgs | Ounces ")
    print("===============")
    listedKgs = 0
    for i in range(5):
        listedKgs = listedKgs + 10
        ounces = listedKgs / 0.02834
        print("",listedKgs, "|","",round(ounces,2))
weightsTable()


# tenth: harder function
# write a function named futureRailFare that uses a for loop to calculate the future value of a train ticket assuming an monthly price rise of 2%

def futureRailFare():
    fareini = float(input("Enter the initial fare: "))
    montini = int(input("Enter the number of months: "))
    for i in range(montini):
        fareini = fareini*1.02
        print("The fare price after",montini,"months is £:",round(fareini,2))
