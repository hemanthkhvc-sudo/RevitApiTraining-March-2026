
# print("Start of the program")


# def greet():
#     print("Hi all")
#     print("Welcome to Revit API Training")
#     print("This is C# Programming")
#     print("Hope you all are not asleep!!!")

def findClashes():
    #get all structural  elements
    #get all MEP elements
    #Check if they intersect each other
    print("Clash detected between Structural Beam 1 and MEP Duct 1")



# greet()


# print("End of the program")



# def add():
#     a = 10
#     b = 20
#     print(a+b)

# a = 100

# add()

# print(a)






def subtract(a, b):
    print(a-b)


def sumOfAllNumbers(*inputs):
    total = 0
    for n in inputs:
        total += n
    print(total)






#void 
#return

# def add(a, b):
#     xyz = 200
#     50*80
#     #snbjlkdhbf
#     print("Something")
#     return a+b



# result = add(10,20)

# new = result * 200


# def checkIfEvenOrOdd(a):
#     if a%2 ==0:
#         print(f"({a} is a Even number)")
#     else:
#         print(f"({a} is a Odd number)")
    
# checkIfEvenOrOdd(11)

# Create a Function, will Accept Parameter and sort even or Odd number 25-03-2026

# def number (x):
#     if x % 2==0:
#         print (x, "is an even number")
#         print (f"{x} is an even" )
#     else:
#         print (x, "is an odd number")

# number(132)


# def evenOrOddFunc (num): # Defining a function named func with parameter num
#     if num%2 ==0:# condition to check whether the num is even
#         print(num," is even number")#  if true print this statement 
#     else:
#         print(num,"is a odd number")# if not true then print this statement
#     return num 
# Num = evenOrOddFunc(3) # Passing the value to be stored in variable


def is_prime(num):
    # Return True if num is prime, else False.
    # A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
 
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def prime(num):
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")


# def calculator(a, b, operation):
#     if operation == "add":
#         return a + b
#     elif operation == "subtract":
#         return a - b
#     elif operation == "multiply":
#         return a * b
#     elif operation == "divide":
#         return a / b
#     else:
#         return "Invalid operation"
    
#     print("END OF FUNCTION")
    

def calculator(a, b, operation):
    result = None
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = a / b
    else:
        result = "Invalid operation"
    return result

# print(calculator(20, 5, "add"))      
#print(calculator(20, 3, "subtract"))  
# print(calculator(20, 2, "multiply"))  
# print(calculator(20, 4, "divide"))



def testFuction():
    x = 10
    20*50
    if 10>2:
        546
    else:
        7899


a = testFuction()
print(a)



