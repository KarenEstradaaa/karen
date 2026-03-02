#_____________3.1 say goodbye________________
name = "Karen"
#print("Goodbye,", name) #prints "Goodbye, Karen"
def say_goodbye(name):
    return name
print("Goodbye", name)

#______________3.2 area of a circle_______________
#area_circle = "3.14r^2"
#print(area_circle)
def area_circle(radius):
    area = 3.14 * radius **2 
    return area
print(area_circle(2)) #prints 12.56!

# _______________4.1 subtract, multiply, divide________________
def subtract(a, b):
    return a - b
print(subtract(1,2)) #prints -1
print(subtract(5,2)) #prints 3
print(subtract(10,3)) #prints 7

def multiply(a, b):
    return a * b
print(multiply(5,2)) #print 10
print(multiply(16,20)) #prints 320
print(multiply(1,100)) #prints 100

def divide(a, b):
    return a / b
print(divide(4,2)) #print 2.0
print(divide(15,3)) #prints 5.0
print(divide(100,10)) #print 10.0

#_____________5.1 what should i wear___________
temperature = [55,60,65,70,75]

def whattowear(temperature):
    minimum = min(temperature)
    maximum = max(temperature)
    return (minimum, maximum)
print(whattowear(temperature)) #prints "(55, 75)"

#__________5.2 check if it's the weekend__________
# monday = 1, tuesday = 2, wednesday = 3, thursday = 4, friday = 5, saturday = 6, sunday = 7
def is_weekend(num):
    if num == 6 or num ==7:
        return True
    else:
        return False
print(is_weekend(2)) #Prints False -> tuesday is not part of the weekend
print(is_weekend(7)) #prints True -> sunday is part of the weekend

#__________________5.3 Fuel Efficiency__________________
def fuel_efficiency(miles, gallons):
    return(miles / gallons)
print(fuel_efficiency(10,2)) #prints 5.0

#________________5.4 Secret Code________________

def secret_code(num):
    last_digit = num % 10
    remainder = num // 10
    digit = len(str(remainder)) #this makes it into a set of text and then counts how many digits in the string
    result = last_digit * (10** digit) + remainder # 5 * 10^4 = 5000 + 1234 = 51234
    return result
print(secret_code(12345)) #prints 51234

#____________6.1 Oski stole your power______________________________
def get_exponent(x,y):
    result = 1
    for i in range(y):
        result *= x 
    return result
print(get_exponent(2,3)) #prints 8!

#_____________6.2 min and max with loops___________ 

#6.2.1 
integers = [7, 9, 2, 5, 4]
def find_min(integers):
    smallest = integers[0]
    for number in integers:
        if number < smallest:
            smallest = number
    return smallest
print(find_min(integers)) #prints 2 which is the minimum number

def find_max(integers):
    largest = integers[0]
    for number in integers:
        if number > largest:
            return number
print(find_max(integers)) #prints 9

#6.2.2
integer = [4, 1, 9, 6, 2]
def find_min(integer):
    smallest = integer[0]
    i=1
    while i < len(integer):
        smallest = integer[i]
        i += 1
        return smallest
print(find_min(integer)) # prints 1

def find_max(integer):
    largest = integer[0]
    i=1
    while i < len(integer):
        if integer[i] > largest:
            largest = integer[i]
        i += 1
    return largest
print(find_max(integer)) #prints 9

#____________6.3 calculate the sum_____________
def find_sum(integer):
    total = 0
    while integer > 0:
        digit = integer % 10
        total += digit
        integer = integer // 10
    return total
print(find_sum(2468)) #prints 20

#_____________7.1________________
number = 2468
result = find_sum(number)
print(f"The result of find_sum with input {number} is {result}.") #prints the result of find_sum with input 2468 is 20
