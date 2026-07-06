# ==============================================================================
# 1. Introduction to Lists
# ==============================================================================
# Creating a list of floating-point numbers
marks = [22.22, 33.21, 45.21, 21.31]
print(marks)
print(type(marks))  # Expected: <class 'list'>

# Accessing list elements using 0-based indexing
print(marks[0])
print(marks[2])

# Getting the total count of elements using len()
print(len(marks))

# Lists can store multiple data types simultaneously
student = ["name", 22.2, "location"]
print(student)

# Mutability: Strings are immutable, but lists are mutable (elements can change)
student[0] = "name2"
print(student)


# ==============================================================================
# 2. List Slicing
# ==============================================================================
marks_list = [22.1, 23.4, 25.6, 33.7, 12.5, 22.9]

print(marks_list[1:4])  # Indices 1, 2, and 3 (ending index is excluded)
print(marks_list[:4])   # Slices from the start (index 0) up to index 4
print(marks_list[1:])   # Slices from index 1 all the way to the end
print(marks_list[-3:-1])  # Negative slicing (reads from right to left)


# ==============================================================================
# 3. List Methods
# ==============================================================================
# Note: Renamed variable 'list' to 'num_list' to avoid shadowing the built-in function
num_list = [2, 1, 3, 45, 7]

# .append(): Adds an element to the very end of the list
num_list.append(12)
print(num_list)

# Note: .append() modifies the list in place and returns None
print(num_list.append(7))  # This will print 'None'
print(num_list)            # This shows the updated list containing the 7

# .sort(): Sorts the list in ascending order by default
num_list.sort()
print(num_list)
print(num_list.sort())  # Note: .sort() also modifies in place and returns None

# Sorting in descending order using reverse=True
num_list.sort(reverse=True)
print(num_list)

# Sorting a list of strings alphabetically
list2 = ["orange", "banana", "mango", "apple"]
list2.sort()
print(list2)

# Sorting a list of strings in reverse alphabetical order
list2.sort(reverse=True)
print(list2)

# .reverse(): Completely reverses the elements of the original list in place
list3 = ['a', 'b', 'd', 'c', 'p', 'z', 'g']
list3.reverse()
print(list3)

# .insert(index, element): Inserts an element at a specific index
list3.insert(2, 'r')
print(list3)

# .remove(element): Removes the first occurrence of a matching element
list3.remove('c')
print(list3)

# .pop(index): Removes and returns the element at a specific index
list3.pop(0)
print(list3)


# ==============================================================================
# 4. Tuples in Python
# ==============================================================================
# Tuples are built-in data types used to create immutable sequences of values
tup = (1, 5, 2, 77, 3)
print(type(tup))  # Expected: <class 'tuple'>
print(tup[0])
print(tup[1])

# This is not possible because tuples are immutable:
# tup[3] = 8  --> Throws a TypeError

# Creating an empty tuple
tup2 = ()
print(tup2)

# Creating a tuple with a single value requires a trailing comma
tup3 = (2,)  # Correct syntax for a single-element tuple
tup4 = (4)   # Incorrect: Python interprets this purely as an integer
print(type(tup3))  # Expected: <class 'tuple'>
print(type(tup4))  # Expected: <class 'int'>

# Note: For multiple values, a trailing comma is completely optional


# ==============================================================================
# 5. Tuple Methods
# ==============================================================================
tup5 = (55, 11, 77, 11, 22, 33, 11)

# .index(): Returns the index of the very first occurrence of an element
print(tup5.index(11))

# .count(): Counts the total number of times an element occurs in the tuple
print(tup5.count(11))


# ==============================================================================
# 6. Practice Questions & Answers
# ==============================================================================

# --- Question 1: WAP to ask the user to enter names of their 3 favorite movies & store them in a list. ---
print("\n--- Movie List Practice ---")
fav_movies = []
fav_movies.append(input("Enter your 1st favorite movie: "))
fav_movies.append(input("Enter your 2nd favorite movie: "))
fav_movies.append(input("Enter your 3rd favorite movie: "))
print("Your favorite movies:", fav_movies)


# --- Question 2: WAP to check if a list contains a palindrome of elements. (Hint: use copy() method) ---
print("\n--- Palindrome Check Practice ---")
test_list = [1, 2, 3, 2, 1]

# Make a shallow copy of the list
list_copy = test_list.copy()
# Reverse the copy in place
list_copy.reverse()

# Compare the original list with the reversed copy
if test_list == list_copy:
    print("The list is a palindrome.")
else:
    print("The list is NOT a palindrome.")


# --- Question 3: WAP to count the number of students with the “A” grade in the following tuple. ---
print("\n--- Tuple Grade Count Practice ---")
# Initializing tuple based on your explicit input sequence: ["C", "D", "A", "A", "B", "B", "A"]
grades_tuple = ("C", "D", "A", "A", "B", "B", "A")

# Count occurrences of "A"
a_count = grades_tuple.count("A")
print(f"Number of students with an 'A' grade: {a_count}")


# --- Question 4: Store the above values in a list & sort them from “A” to “D” ---
print("\n--- List Sorting Practice ---")
# Convert tuple to list
grades_list = list(grades_tuple)

# Sort alphabetically (Ascending: 'A' to 'D')
grades_list.sort()
print("Sorted grades list:", grades_list)