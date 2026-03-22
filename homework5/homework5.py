#Homework 5

#_________________homework 1 + 2 Review_______________________

''' 
#1
Git: is a software that keeps track and holds files that can be changed or altered. a version control 
system that tracks changes in code over time. it works locally on our computers 

github: a website that hosts git repositories online. It lets you store/share/collaborate on projects
'''

'''
#2
Command line: where you eneter commands and can write out your code
Terminal: outputs the commands in the command line and actually runs the code
'''

'''
#3
local repository: the copy on your computer
remote repository: the copy on github
'''

'''
#4

Version control: a system that records changes to files over time so that specific versions can be recalled later
'''

'''
#5 
Staging area: a temporary "holding zone" where you prepare changes before saving them permanently
'''

'''
#6
git add: allows you to save all of your files
'''
'''
#7
git commit: allows you to save your changes locally. moves changes from staging area to version history
'''

'''
#8
git push: tells your local repository to save changes to your remote repository
'''

'''
#9
git status: display the current state of the working directory and the staging area
'''

'''
#10
git pull: update your current local working branch with the latest changes from a remote repository
'''

'''
#11
pwd: prints the current working directory
'''

'''
#12
ls: list all of the contents in the current directory 
'''

'''
#13
cd: changes director, Use it to move from one folder to another 
'''

'''
#14 
nano: lets you edit a file direclty on the terminal
'''

'''
#15
touch: lets you create a file in current direcotory
'''

'''
#16
mv: lets you move a file into another directory
'''

'''
#17
rm: removes a file or delete it 
'''

'''
#18
cat: Tells your computer to print out all the contents of a file
'''

#________________3.2 directory tree______________
# a. pwd

# b. ls

# c. 
# - cd.. 
# - cd brianna_repo
# -git pull origin main

# d. mv homework.py ~python_decal/judy_decal/homework

# e. cd ..
# - cd judy_decal
# - cd homework

# f. cat homework.py

# g. gid add .
# git commit -m "done with hw"
#git push origin main


# h.  the error means that she tried to push it without first pulling the newest changes from the remote repository.
#     she needs to use git pull origin main. after it finishes she should run git push origin main again.

# i. c~
#    cd recent

#____________________4.1 Data Types_______________ 
def checkDataType(x):
    return type(x).__name__

print(checkDataType(3.14)) #prints float
print(checkDataType(True)) #prints bool

#____________________4.2 conditions_______________ 
def evenOrOdd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(evenOrOdd(7)) #prints odd
print(evenOrOdd(10)) #prints even

#__________________5 loops____________
numbers = [1,2,3,4,5]

def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sumWithLoop(numbers)) #prints 15

#__________6.1 List____________
lst = ['a','b', 'c']

def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list

print(duplicateList(lst)) # prints ['a', 'a', 'b', 'b', 'c', 'c']

#__________________6.2 Debugging______________________________________
def square(num): # was missing the :
    return num * num
print(square(5)) #prints 25

#_______fav function____________
result = duplicateList(['a', 'b', 'c'])
print(result)