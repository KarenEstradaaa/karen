#_____________3.1 List Operators______________________________
ls = ['pasta','tamales','burrito', 'mango', 'cookies' ]
print(ls[2])
print(ls[-1])

ls.append('waffle') 

'''I encountered a SyntaxError: unterminated string literal (detected at line 5)
I originally wrote ls.append('waffle) I forgot to include the ' to end the string, I fixed it by adding it.
'''

print(ls) # prints ['pasta', 'tamales', 'burrito', 'mango', 'cookies', 'waffle']
ls.insert(0, 'apple') #inserts apple in the start of the list
print(ls) #prints ['apple', 'pasta', 'tamales', 'burrito', 'mango', 'cookies', 'waffle']
ls.remove('tamales')
print(ls) #prints ['apple', 'pasta', 'burrito', 'mango', 'cookies', 'waffle']
print(len(ls)) #prints 6

for food in ls:
    print(food.upper()) #prints APPLE PASTA BURRITO MANGO COOKIES WAFFLE all one top of each other
'''AttributeError: 'list' object has no attribute 'upper'. 
I originally printed "print(ls.upper(ls)." which didn't work because it should have been food to be consistent.
and nothing inside the (). I fixed it to be print(food.upper()).
'''
print(ls[0::5]) #prints ['apple', 'waffle']
if "potato" in ls:
    print("A potato!")
else: 
    print("No potato!") #prints No potato!

#__________________3.2 Slicing and Striding___________________________
numbers = list(range(21)) 
def get_first_15(numbers):
    return numbers [:15] 
print(get_first_15(numbers)) #prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
'''SyntaxError: expected ':'
I put def get_first_15(numbers). -> I forgot to put a :, I changed it to get_first_15(numbers): '''

lst= get_first_15(numbers)
def get_every_5th(lst):
    return lst[::5]
print(get_every_5th(lst)) #prints [0,5,10]

def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]
print(reverse_and_stride(lst))

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2) #prints [14, 11, 8, 5, 2]

#___________________________3.3 Nested List_________________
numbers = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]
print(numbers[2]) #prints [7, 8, 9]
print(numbers[1][1]) #prints 5
numbers.append([10, 11, 12])
print(numbers) #prints [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

def sum_nested(numbers):
    total = 0
    for row in numbers:
        for num in row:
         total += num     # add to total
    return total 
print(sum_nested(numbers)) #prints 78

#____________________________3.4 Create a 5x5 list____________________
def five_by_five():
    nested_list = []
    count = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(count)
            count += 1
        nested_list.append(row)
    return nested_list
#print(five_by_five()) makes it into a very long string of lists and doen't format rows and columns
for row in five_by_five(): #this makes it so the rows are stacked and coloumns side by side
    print(row)

def replace(grid):
    new_grid = []
    for row in grid():
        new_row = ["?" if num % 3 == 0 else num for num in row]
        new_grid.append(new_row)
    return new_grid
for row in replace(five_by_five):
    print(row)

def sum_of_replace(grid):
    count = 0 
    for row in grid:
        for value in row:
            if value != "?":
                count += value
    return count
print(sum_of_replace(replace(five_by_five))) #prints 217

#______________4.1 Dictionary Operations________________________
ages = {
    "Katie": 30,
    "Marium": 42,
    "Safia": 25,
    "Mira": 48
}
print(ages['Katie']) #prints 30
ages["Mira"] = 100
print(ages) #prints {'Katie': 30, 'Marium': 42, 'Safia': 25, 'Mira': 100}
ages["Milana"] = 52
print(ages) #prints {'Katie': 30, 'Marium': 42, 'Safia': 25, 'Mira': 100, 'Milana': 52}
del ages['Marium']
print(ages) #prints {'Katie': 30, 'Safia': 25, 'Mira': 100, 'Milana': 52}
for key, value in ages.items ():
    print(f"{key} = {value}") #prints Katie = 30, Safia = 25, Mira = 100, Milana = 52 as one column

#___________favorite function________________
ls = ['pasta','tamales','burrito', 'mango', 'cookies' ]
ls.append('waffle')
print('result is', ls) #prints result is ['pasta', 'tamales', 'burrito', 'mango', 'cookies', 'waffle']