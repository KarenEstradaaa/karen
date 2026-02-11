# File: homework1.py
# --- Variables and Data Typles ---
a=10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals
b=1.5
print(b)
print(type(b)) # b is float, a fractional number or a number with decimals
c=3j
print(c)
print(type(c)) # c is complex, represents numbers with both real and imaginary parts (complex numbers)
d="hello"
print(d)
print(type(d)) # d is strings, represents words or text
e= [1, 2, 3]
print(e)
print(type(e)) # e is a list, which holds a collection of items
f= {"Karen", "mangos"}
print(f) # f is a set, used to store multiple items in a single variable
print(type(f))
g = (1, 2)
print (g)
print(type(g)) # g is a tuple, tuples are used to store multiple items in a single variable
h=["apple", "banana", "straberry"]
print(h)
print(type(h)) #h is a list
i= True
print(i)
print(type(i)) # i is a bool, it represents two truth values
j= None
print(j)
print(type(j)) # j is a NoneType, 
k= [True, "blue", 12]
print(k)
print(type(k)) # k is a list
l = str(14)
print(l)
print(type(l)) # l is a strings
m= 1e4
print(m)
print(type(m)) # m is a float

# 1. I found 9 different data types
# 2. the data types I found are integer, float, complex, strings, list, set, tuple, bool, and nonetype.
# 3. the variables that have the same data type: h,e and k, e and l,  b and m.
# 4. l is not an but a string because it converts 14 into string 14. str(14) makes the numerical 14 into text.
# 5. dict = dictionary. it creates a collection which is unordered and can be changed

# --- Booleans ---
print(10>9) # True, 10 is greater than 9
print (10==9) # False, 10 does not equal 9
print (10<=9) #False
bool("abc") # True
bool(123) # True 
bool(["apple","cherry", "banana"]) #true
bool(True) # True
bool(False) # False
bool(0) # False
bool("") # False
bool(" ") # True
bool (()) # False
bool([]) # False, doesn't like empty things
bool({}) # False
bool(True and False) # False, false is not true (both have to be true)
bool(True and True) # False
bool(False and False) # False
bool(True or False) # True
bool (True or True) # True
bool(False or False) # False
bool(not(False)) # True
bool(not(True)) # False

# 1. some values are automatically treated as false like (), {}, 0
# 2. bool(" ") being true but bool("") being false and the sensitivity or using AND or OR
# 3. bool(6<7) this will result in true because 7 is greater than 6
# 4. bool(15>20) this will result in false because 15 is NOT greater than 10

# --- Arithmetic Operators ---
print(10+5) # 15, + preforms addition
print(10-5) # 5, - preforms subraction
print(2*4) # 8, * preforms multiplication
print(6/3) # 2.0, / prefroms division
print(5%2) # 1, % shows the modulus, think of it like 2 can fit into 5 twice and there is one left over
print(3**2) # 9, ** acts like an exponent
print(15//2) # 7, // divides the numerator by the demonimator and rounds to nearest whole number

# --- Comparison Operators ---
print(5==2) # False, 5 does not equal 2
print (10 != 10) # False, 10! does not equal 10
print(2<5) # True, 5 is greater than 2
print(12>5) # True
print(5<=6) # True
print(1>=10) # False

# --- Assignment Operators ---
x=5
x += 5
print(x) # answer is 10
x=5
x -= 4
print(x) # answer is 1
x=5
x *= 3
print(x) # answer is 15

# --- Logical Operators ---
# 1. The operator and makes it so that both have to be true or both have to be false.
print(True and True) # True
print(True and False) # False
'''
 2. the or operator makes it so that if either option is true, 
            it will be show up true for all of them.'''
print(True or False) # True
print(False or False) #False
#3 the operator not makes it so it reverses the truth value in a statement/opposite answer
print(not(True)) # False
print(not(False)) # True

# --- More questions ---
'''
1. / prefroms division, while // divides the numerator by the 
demonimator and rounds to nearest whole number

2. % shows the modulus, think of it like 2 can fit into 5 twice and there is one left over 
while // divides the numerator by the demonimator and rounds to nearest whole number

3. I think you would use the % because that shows the values that 
can't be divided (remainder)

4. assignment operators assign a value to a varible using the = function,
once defined you can use that variable to solve arithmetical problems that can be printed,
by print(variable) and recieve an output!

'''
# --- Strings ---
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # prints h
print(my_string[1]) # prints e
print(my_string[2]) # prints l
print(my_string[3]) # prints l
print(my_string[4]) # prints o
print(my_string[-1]) #prints o
print(my_string[1:3]) # Prints el
print(my_string[0:5:2]) #prints hlo
print(len(my_string)) #prints 5, it prints how many words it is
print(my_string + "goodbye") # Prints hellogoodbye, it combines the two words into one without spaces
print(my_string*7) # Prints : hellohellohellohellohellohellohello, prints the word that many times

# --- Questions ---
'''
1. the term slicing is a method for extracting specific 
portions of sequences. This can be used for strings, lists, tuples, and ranges. For the mutations 1-9
we used this method to slice our string.
'''

#2
name="Oski"
print("hello, my name is", name) # Prints : hello, my name is Oski

#3
name = "Oski"
print(f"hello, my name is {name}") # prints: hello my name is Oski

'''# 4. f-strings use f in the begining of a string and replaced the variable in the {} 
with the value defined above. The only difference in the two is the way they're formated'''

# --- Terminal Commands ---

#cd : Change directory
#Changes directories. Use it to move from one folder to another 
# ex: cd Desktop

#ls = list
# list all the contents of the folder you are in (other folders and files but NOT hidden ones)
# Ex: you would type "ls" in terminal

#ls -a
# this shows hidden files 
# ex: "ls -a" in terminal

#mkdir = make directory
# this is used to make a new folder on the terminal
# to do this you would do mkdir <name of new folder> ex: mkdir karen

#cat = concatenate
# Tells your computer to print out all the contents of a file
# ex: "cat homework1.py" in terminal 

#pwd = print working directory
# this will tell your command line to print the current working directory
# you would just type in "pwd" and it should tell you what folder you are in

#cd ..
# another type of change directory, this moves you up to the parent directory
# Ex: "cd .." in terminal 

#cd .
# this does nothing? it means to change directories in the one you already are in. so there should be no effect
# ex: "cd ." in terminal 

#cd ~
# another type of change directory, this one takes you directly to your home directory
# ex: "cd ~" in terminal

#cp = copy
# this allows you to make a copy of a file and rename it
# cp <source_file> <destination_file>      ex:  cp testproject.py finalproject.py

#mv = move
# this is used to move files and rename files
# ex: mv <old name> <new name> 

#rm = remove
# Allows you to remove a file/delete it
# ex: rm homework1.py

#clear
# this will clear all of the commands and outputs from the terminal
# ex: "clear" in terminal

#grep
# allows you to search for a specific set of characters inside a file
# ex: grep [term] [filename]  ex: grep hello datatypes.py

''' # 1. whoami comand: it will tell you which user you are currently logged in as
          ex: "whoami" in terminal should appear with my user name ex: whoami shows up as karen
        date command: this will show you the date and time in which you asked for the command
        ex: date in terminal prints Wed Feb 4 17:37:57 PST 2026
        find comand: helps you find a file in a location you specify
            to use you would use find [path] [options] [expression] in terminal
'''

''' #2. ls list everything in your current working directory except hidden files. 
ls -a shows everything including hidden files'''

#3. a hidden file is a file or directory that isn't found using common command tools

'''4. flag: --help : gives a short description of all command line options.
                      to use it "command --help"     ex: cp --help
    flag: --version : tells you what version of the program you are using
                      to use it you need to type in "python --version" and a very long message should appear
    Flag: --l : list specific details of a file size, permissions, date, owner
                to use it you would use "ls homework1.py -l"
'''