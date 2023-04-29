# String's
str1 = "alpha"
str2 = 'beta'
str3 = '''gamma string'''
str4 = """delta string"""

# Numbers
num1 = 123
flt1 = 2.0

# List / Collection of multi datatypes, enclosed in square brackets.
first_list = [str1, "DevOps", 45, num1, 1.5]

# Printing a List
print(first_list)
print(first_list[0])

first_list[1] = "SysOps"
print(first_list[1])

print()

# Tuple / collection of multi datatype, enclosed in round bracket = immutable values
first_tuple = (str1, "DevOps", 45, num1, 1.5)

# Printing a Tuple
print(first_tuple)
print(first_tuple[1])

print()

# Dictionary / Elements in the dictionary are always in pairs(Key:Value), curly braces.
first_dictionary = {"Name":"Arfel", "Weight":60, "Height":175, "Exercises":["Boxing", "Dancing", "Jogging", "Sex"]}

# Printing a dictionary
print(first_dictionary)
print(first_dictionary["Name"],"'s hobby is", first_dictionary["Exercises"])

print()

print("Variable first_list is a:", type(first_list))
print("Variable first_tuple is a:", type(first_tuple))
print("Variable first_dictionary is a:", type(first_dictionary))

print()

# Boolean
x = True
y = False

# Printing Boolean
print(x)
print(y)

print("x is a", type(x))
print("y is a", type(y))