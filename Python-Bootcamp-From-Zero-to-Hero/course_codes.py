# 14 Variable Assignments
print('\n******** Episode 14 ********\n')
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)
print(type(my_taxes))

# 15 Introduction to Strings
print('\n******** Episode 15 ********\n')
print("hello \t world")
print("hello \n world two")
print(len("hello"))

# 16 Indexing and Slicing with Strings
print('\n******** Episode 16 ********\n')
mystring = "abcdefghijk"
print(mystring[3:6]) #The output is: def
print(mystring[::3]) #The output is: adgj Because we chose 3 reading steps
print(mystring[::-1]) #The output is: kjihgfedcba / This is a trick to reverse the string

# 17 String Properties and Methods
print('\n******** Episode 17 ********\n')
letter = "z"
print(letter * 10)
x = "Hello World"
x.upper()
x.lower()
x.split() #The output is: ['Hello', 'World']
x.split('l')#The output is: ['He', '', 'o Wor', 'd']

# 19 Print Formatting with Strings
print('\n******** Episode 19 ********\n')
print("This is a string {}".format("INSERTED"))
print("The {0} {0} {0}".format("fox", "brown", "quick"))  #The output is: The fox fox fox
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick")) #The output is: The quick brown fox
result = 100/777
print("The result was {r:1.3f}".format(r=result))
name = "Sam"
age = 3
print(f'{name} is {age} years old.')

# 21 Lists in Python
print('\n******** Episode 21 ********\n')
new_list = ["one", "two", "three", "four", "five"]
new_list.append('six') #The output is:["one", "two", "three", "four", "five",'six']
new_list.pop() #The output is:["one", "two", "three", "four"]
new_list.sort()#The output is:['five', 'four', 'one', 'three', 'two']
new_list.reverse()#The output is:['five', 'four', 'three', 'two', 'one']

# 23 Dictionaries in Python
print('\n******** Episode 23 ********\n')
d = {"k1": 123, "k2": [0, 1, 2], "k3": {"insidekey": 100}}
print(d["k3"]["insidekey"])
d["k1"] = "NEW VALUE"
d["k4"] = 54
d.keys
d.values
d.items

# 25 Tuples with Python
print('\n******** Episode 25 ********\n')
t = ("a", "a", "b")
t.count("a")
t.index("b")

# 26 Sets in Python
print('\n******** Episode 26 ********\n')
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
set(mylist)  #The output is: {1, 2, 3}

# 27 Booleans in Python
print('\n******** Episode 27 ********\n')
1 > 2  # The output is: False
1 == 1  # The output is: True
b = None # The output is: nothing