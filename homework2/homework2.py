# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?

'''
Git: is a software that keeps track and holds files that can be changed or altered. a version control 
system that tracks changes in code over time. it works locally on our computers 
github: a website that hosts git repositories online. It lets you store/share/collaborate on projects
Git bash: an application for windows environments which allows you to execute git command lines 
'''

# 2) What’s the difference between the terminal and the command line?

'''
Command line: where you eneter commands and can write out your code
Terminal: outputs the commands in the command line and actually runs the code
'''

# 3) How does Windows PowerShell differ from Git Bash?

'''
Windows powershell is microsoft's shell built specifically for window devices, however it still runs 
commands and acts like a terminal. Git bash allows interaction between git repositories from a windows command
line but not the default one. 
'''

# 4) What’s the difference between Anaconda, conda, and Python?

'''
Anaconda is a open-source distribution of various python packages like Jupyter and RStudio. It specifically
run python language
Conda is the package manager of Anaconda. It allows you to use command line tools.
Python: is a programing language that can be run and intrepreted in Anaconda. 
'''

# 5) What is VS Code? 

'''
VS code is a python editor that lets you write and edit python code and runs it through a built in terminal.
It runs a variety of different languages through its extension features. 
'''

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?

'''
Jupyter Notebook: simple interface which allows us to open notebooks, terminals, and text files. 
It is primarily used for data analysis and visualization. It only allows for single-document editing. 
Jupyter Lab: offers a very interactive interface that lets you access notebooks, consoles, terminals. Allows
you to open multiple documents in seperate tabs.
'''

# 7) What does ~/ mean?

'''
means starting from the home directory. For example if i was in users/karen/Python_decal26/lecturenotes and 
send the command cd ~/ it would send me back to my home directory users/karen
'''

# 8) What’s the difference between an absolute path and a relative path?

'''
Relative Path: when you go from your current compisition onyour computer, and go through each folder individually
Absolute path: when you go from your home directory to a file all the way to the exact location of that file
'''

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".

'''
Relative Path: course_assingments/homework2 
Absolute Path: users/karen/Python_decal26/course_assignments/homework2
'''

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?

'''
you would use command cd ..
'''

# 11) What would rm ./ do in your current directory? (Don’t try it!)

'''
Allows you to remove a file/delete it
'''

# 12) What do the following commands do?
# git add = allows you to save all of your files
# git commit = allows you to save your changes locally. moves changes from staging area to version history
# git push = tells your local repository to save changes to your remote repository

# 13) What's the difference between "git add ." and "git add <file>"?

'''
git add saves ALL of your files, while git add <file> save only that specific file
'''

# 14) What do "git status" and "git log -1" do?
'''
git status shows the current state of your working directory and staging area
git log -1: shows all the commits that have changed a given file
'''

# 15) What’s the difference between cloning a repository and pulling from it?
'''
cloning a repository copies all files to the local machine, while pulling from it only copies the modified 
files to the local machine. 
'''

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
'''
I had done the very first lecture material on my own time and I kept getting an error saying that there was
no path connected to vs code or something, so I reached out to my friend Hannah who helped me solve this issue!
'''
# 17) What’s a question you still have? What’s something you’re confused about?
'''
I'm still confused about the differences between Jupyter notebook and lab. As well as windows powersehll
and Git Bash.
'''

# 18) Tell me a fun fact!
'''
Platypusses glow under UV light! It was a recent discovery!
'''

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)
print(27//5) 
'''idk why this is my favorite but I found it so cool when I did it in the last homework but
it divides your numerator by the denominator and rounds to the nearest whole number'''