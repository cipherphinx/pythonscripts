# Defining Function
"""
def add(num1, num2):
    total = num1 + num2
    return total

out = add(2, 3)
print(out)


def adder(num1, num2):
    total = num1 + num2
    print(total)

adder(10, 50)
print(adder(10, 50))
"""

def summ(arg):
    x = 0
    
    for i in arg:
        x = x + i
    
    return x
    
#out = summ([10,20,30])
#print(out)

#summ([10, 20], [30, 50])

# Default Argument

def greetings(msg="Morning"):
    print(f"Good {msg}")
    print("Welcome to the function.")

greetings()
greetings("Evening")