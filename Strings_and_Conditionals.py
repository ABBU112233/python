# ==============================================================================
# 1. String Literals & Creation Ways
# ==============================================================================
# Double quotes allow single quotes inside the string seamlessly
str1 = "this is a string it's for example"
print(str1)

# Single quotes allow double quotes inside the string seamlessly
str2 = 'also a string " can be used in between'
print(str2)

# Triple quotes allow multi-line strings or docstrings
str3 = """one more way to write string"""
print(str3)


# ==============================================================================
# 2. Escape Sequence Characters
# ==============================================================================
# \n creates a newline (moves the text after it to the next line)
str4 = "this is a apple \nit costs 2$"
print(str4)

# \t creates a horizontal tab space
str5 = "this creates a tab \t space in between"
print(str5)


# ==============================================================================
# 3. String Operations
# ==============================================================================
# Concatenation: Joining strings together
str1 = "hello"
str2 = "world"
print(str1 + str2)  # Outputs: helloworld

# Adding a space between strings during concatenation
str5 = str1 + " " + str2

# Length function: len() returns the total character count (including spaces)
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))
print(len(str5))  # Space is also counted in the length


# ==============================================================================
# 4. String Indexing
# ==============================================================================
# Indexing helps to access individual characters based on position (starts from 0)
str6 = "vs code"
print(str6[3])

# Strings are immutable: You cannot assign or mutate individual characters directly
# e.g., str6[0] = 'V' will throw a TypeError


# ==============================================================================
# 5. String Slicing
# ==============================================================================
# Accessing parts of a string: str[start_index : end_index] (end_index is excluded)
str7 = "stringslicing"
print(str7[2:6])  # Extracts indices 2, 3, 4, and 5
print(str7[:7])   # Slices from the start (index 0) up to index 7
print(str7[6:])   # Slices from index 6 all the way to the end


# ==============================================================================
# 6. Negative Indexing
# ==============================================================================
# Negative index reads from right to left (starts from -1)
str8 = "apple"
print(str8[-3:-1])  # Extracts indices -3 and -2 ('pl'), ending index is excluded


# ==============================================================================
# 7. String Functions
# ==============================================================================
str9 = "this is string used to demonstrate functions"

# .endswith(): Returns True if the string ends with the specified suffix
print(str9.endswith("ions"))

# .capitalize(): Capitalizes only the very first letter of the string
print(str9.capitalize())  # Note: This returns a copy, it does not change the actual variable

# Modifying the original variable by re-assigning it
str9 = str9.capitalize()
print(str9)

# .replace(old, new): Replaces occurrences of a substring with a new substring
print(str9.replace("o", "a"))
print(str9.replace("is", "was"))

# .find(): Searches for a substring and returns its starting index (returns -1 if not found)
print(str9.find("g"))
print(str9.find("used"))

# .count(): Counts total occurrences of a substring
print(str9.count("o"))
print(str9.count("is"))


# ==============================================================================
# 8. Conditional Statements
# ==============================================================================
# 'if' statement execution
age = 21
if age > 18:
    print("you are eligible")
    print("for voting")

# 'if-elif-else' chain execution (proper indentation defines code blocks in Python)
light = "green"
if light == "red":
    print("stop")
elif light == "green":
    print("go")
else:
    print("wait")


# ==============================================================================
# 9. Practice Questions & Answers
# ==============================================================================

# --- Question 1: WAP to ask the user to enter names of their 3 favorite movies & store them in a list. ---
print("\n--- Movie List Practice ---")
movies = []
# Appending inputs individually to build the list
movies.append(input("Enter your 1st favorite movie: "))
movies.append(input("Enter your 2nd favorite movie: "))
movies.append(input("Enter your 3rd favorite movie: "))

print("Your favorite movies list:", movies)


# --- Question 2: WAP to check if a list contains a palindrome of elements. (Hint: use copy() method) ---
print("\n--- Palindrome List Practice ---")
# Example list setup (can be changed to test)
original_list = [1, 2, 3, 2, 1]

# Copy the original list to preserve it
list_copy = original_list.copy()
# Reverse the copied list in place
list_copy.reverse()

# Compare original list with its reversed copy
if original_list == list_copy:
    print("The list is a palindrome.")
else:
    print("The list is NOT a palindrome.")


# --- Question 3 & 4: Tuple Operations and Sorting Lists ---
# WAP to count the number of students with the “A” grade in the following tuple.
# Store the above values in a list & sort them from “A” to “D”.
print("\n--- Tuple/List Grade Practice ---")

# Defining the initial tuple containing student grades
grades_tuple = ("A", "B", "C", "A", "D", "B", "A", "C")

# Counting "A" grades using the tuple .count() method
count_A = grades_tuple.count("A")
print(f"Number of students with an 'A' grade: {count_A}")

# Converting the tuple to a list to make it mutable
grades_list = list(grades_tuple)

# Sorting the list in ascending order ('A' to 'D')
grades_list.sort()
print("Sorted grades list:", grades_list)