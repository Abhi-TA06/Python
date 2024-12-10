# Arithmetic Operators
a, b = 10, 3
print("Arithmetic Operators:")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation
print("a // b =", a // b)  # Floor Division

# Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater than or equal to
print("a <= b:", a <= b)  # Less than or equal to

# Logical Operators
print("\nLogical Operators:")
x, y = True, False
print("x and y:", x and y)  # Logical AND
print("x or y:", x or y)    # Logical OR
print("not x:", not x)      # Logical NOT

# Assignment Operators
print("\nAssignment Operators:")
c = 5
print("c =", c)  # Assign
c += 2
print("c += 2 ->", c)  # Add and assign
c -= 1
print("c -= 1 ->", c)  # Subtract and assign
c *= 3
print("c *= 3 ->", c) 

#Truth table of 'or'
print("true or False is ",True or False)
print("true or True is ",True or True)
print("False or True is",False or True)
print("False or False is",False or False)

#Truth table of 'and'
print("true and False is ",True and False)
print("true and True is ",True and True)
print("False and True is",False and True)
print("False and False is",False and False)

print(not(True))