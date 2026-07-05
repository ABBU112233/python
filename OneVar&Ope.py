# ==============================================================================
# 1. Basic Output
# ==============================================================================
# Print a standard greeting string to the console
print("hello world")

# Print an integer directly
print(27)


# ==============================================================================
# 2. Variables and Dynamic Typing
# ==============================================================================
name = "apple"  # String variable representing the product name
price = 25.99   # Float variable representing the price
slot = 12       # Integer variable representing the slot number
new = True      # Boolean variable indicating if the product is new
a = None        # NoneType variable representing the absence of a value

# Print a concatenated string message using the variables
print("The product name is ", name + " its price is ", price)


# ==============================================================================
# 3. Checking Data Types
# ==============================================================================
# Display the data type of each variable using the built-in type() function
print(type(name))   # Expected: <class 'str'>
print(type(price))  # Expected: <class 'float'>
print(type(slot))   # Expected: <class 'int'>
print(type(new))    # Expected: <class 'bool'>
print(type(a))      # Expected: <class 'NoneType'>


# ==============================================================================
# 4. Program to Calculate Sum
# ==============================================================================
"""
Write a program to calculate and display 
the sum of two numbers.
"""
a = 12
b = 13
sum_result = a + b  # Avoid using 'sum' as a variable name since it's a built-in function
print(sum_result)


# ==============================================================================
# 5. Arithmetic Operators
# ==============================================================================
a = 5
b = 2

# Addition operator
print(a + b)

# Subtraction operator
print(a - b)

# Multiplication operator
print(a * b)

# Division operator (always returns a float in Python 3)
print(a / b)

# Modulo operator (returns the remainder of the division)
print(a % b)

# Exponentiation operator (a raised to the power of b)
print(a ** b)


# ==============================================================================
# 6. Relational (Comparison) Operators
# ==============================================================================
a = 25
b = 15

# Equal to comparison
print(a == b)

# Not equal to comparison
print(a != b)

# Greater than or equal to comparison
print(a >= b)

# Less than or equal to comparison
print(a <= b)

# Strictly greater than comparison
print(a > b)

# Strictly less than comparison
print(a < b)


# ==============================================================================
# 7. Assignment Operators
# ==============================================================================
num = 10

# Add and assign: num = num + 10
num += 10
print("num :", num)

# Subtract and assign: num = num - 5
num -= 5
print("num :", num)

# Multiply and assign: num = num * 5
num *= 5
print("num :", num)

# Divide and assign: num = num / 2
num /= 2
print("num :", num)

# Modulo and assign: num = num % 3
num %= 3
print("num :", num)

# Exponentiate and assign: num = num ** 10
num **= 10
print("num :", num)


# ==============================================================================
# 8. Logical Operators
# ==============================================================================
a = 10
b = 20

# Logical NOT operator (inverts the boolean value)
print(not True)
print(not (a > b))

# Logical AND & OR operators
val1 = True
val2 = False

# AND operator: Returns True only if both conditions are True
print("and operator:", val1 and val2)

# OR operator: Returns True if at least one condition is True
print("or operator:", val1 or val2)


# ==============================================================================
# 9. Type Conversion (Implicit) vs Type Casting (Explicit)
# ==============================================================================
a = 10
b = 15.5

# Implicit Conversion: Python automatically converts integer 'a' to float to perform the operation
sum_val = a + b
print(sum_val)

# Explicit Type Casting: Manually converting a numeric string "3" into an integer
a = int("3")
b = 22.3
print(a + b)


# ==============================================================================
# 10. User Input handling
# ==============================================================================
# Reading user input as a string (default behavior)
name = input("enter your name: ")
print("Welcome ", name)
print(type(name))  # Note: The input() function always converts any input into a string

# Reading user input and explicitly casting it to an integer
val = int(input("enter your age: "))
print(type(val))


# ==============================================================================
# 11. Practice Questions & Solutions
# ==============================================================================

# --- Question 1: WAP to check if a number entered by the user is odd or even. ---
# Read an integer from the user
num_check = int(input("Enter a number to check if it's odd or even: "))

# Logic: Even numbers are perfectly divisible by 2 (remainder is 0)
if num_check % 2 == 0:
    print(f"{num_check} is an Even number.")
else:
    print(f"{num_check} is an Odd number.")


# --- Question 2: WAP to find the greatest of 3 numbers entered by the user. ---
# Read three distinct numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Logic: Use conditional statements (if-elif-else) to find the largest value
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

print(f"The greatest of the three numbers is: {greatest}")


# --- Question 3: WAP to check if a number is a multiple of 7 or not. ---
# Read an integer from the user
mult_check = int(input("Enter a number to check if it's a multiple of 7: "))

# Logic: If a number is a multiple of 7, dividing it by 7 leaves a remainder of 0
if mult_check % 7 == 0:
    print(f"{mult_check} is a multiple of 7.")
else:
    print(f"{mult_check} is NOT a multiple of 7.")