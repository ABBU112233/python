# ==============================================================================
# 1. Introduction to Dictionaries
# ==============================================================================
# Dictionaries are used to store data values in key:value pairs.
# They are unordered, mutable (changeable), and do not allow duplicate keys.
info = {
    "key": "value",
    "name": "dictionary",
    "learning": "python",
    "age": 22,
    "subjects": ["c", "java", "python"],  # Lists can be stored as values
    "topics": ("dict", "set"),            # Tuples can be stored as values
    11: 21.22                             # Keys can be integers too
}
print(info)
print(type(info))  # Expected: <class 'dict'>

# Accessing dictionary values using keys
print(info["key"])
print(info["topics"])
print(info[11])

# Dictionaries are mutable: You can overwrite existing values
info["name"] = "new dictionary"
print(info)

# You can also add brand-new key-value pairs dynamically
info["name2"] = "new name added"
print(info)

# Creating an empty dictionary
null_dict = {}
print(null_dict)


# ==============================================================================
# 2. Nested Dictionaries
# ==============================================================================
# A dictionary can store another dictionary inside it as a value
student = {
    "name": "coder",
    "subjects": {
        "phy": 91,
        "chem": 88,
        "math": 93
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])  # Accessing an element inside the nested dictionary


# ==============================================================================
# 3. Dictionary Methods
# ==============================================================================
# .keys(): Returns a view object containing all the keys
print(student.keys())
# Type casting the keys view into a standard list
print(list(student.keys()))

# .values(): Returns a view object containing all the values
print(list(student.values()))

# .items(): Returns key-value pairs as a list-like view of tuples
print(student.items())
pairs = list(student.items())
print(pairs[0])

# Safe value retrieval: comparing bracket notation vs the .get() method
print(student["name"])
print(student.get("name"))

# Behavior with missing keys:
# print(student["name2"])      # This would crash the program with a KeyError!
print(student.get("name2"))    # Safe: returns 'None' instead of throwing an error

# .update(): Inserts or updates specified items from another dictionary/iterable
student.update({"city": "hyderabad"})
print(student)

new_dict = {"state": "TS"}
student.update(new_dict)
print(student)


# ==============================================================================
# 4. Introduction to Sets
# ==============================================================================
# A set is an unordered collection of items. 
# Every element must be unique, and the elements themselves must be immutable.
collection = {2, 4, 3, 6}
print(collection)
print(type(collection))  # Expected: <class 'set'>

# Sets automatically ignore duplicate values
collection2 = {1, 1, 2, 3, 4, "hello", 'w', 'w', 5}
print(collection2)      # Duplicates are automatically stripped out
print(len(collection))

# Empty collection syntax warning:
collection3 = {}         # WARNING: This creates an empty dictionary, NOT a set!
print(type(collection3)) # Expected: <class 'dict'>

# The correct way to initialize an empty set is using set()
collection4 = set()
print(type(collection4)) # Expected: <class 'set'>


# ==============================================================================
# 5. Set Methods
# ==============================================================================
# Sets are mutable collections, but the individual elements inside must be immutable.
collection4.add(1)
collection4.add(2)
collection4.add(2)  # Duplicates are ignored
collection4.add("apple")
collection4.add((1, 3, 10))  # Tuples are immutable, so they can be added to a set
# collection4.add([1, 2])    # TypeError: Lists are mutable and cannot be added

print(collection4)
print(len(collection4))

# .remove(): Removes the specified element from the set
collection4.remove(1)
print(collection4)

# .clear(): Clears all elements, leaving the set completely empty
collection4.clear()
print(len(collection4))

collection4 = {"apple", "mango", "banana", "watermelon", "strawberry", "pineapple"}

# .pop(): Removes and returns an arbitrary (random) element from the set
collection4.pop()
print(collection4)
print(collection4.pop())


# ==============================================================================
# 6. Important Set Math Operations (Union & Intersection)
# ==============================================================================
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# .union(): Combines values from both sets, returning a fresh, unique set
print(set1.union(set2))  # Outputs: {1, 2, 3, 4, 5, 6}
print(set1)              # Original set remains unchanged
print(set2)              # Original set remains unchanged

# .intersection(): Extracts only the elements present in both sets
print(set1.intersection(set2))  # Outputs: {3, 4}
print(set1)
print(set2)


# ==============================================================================
# 7. Practice Questions & Answers
# ==============================================================================

# --- Question 1: Store word meanings in a dictionary ---
print("\n--- Word Dictionary Practice ---")
word_dict = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
}
print(word_dict)


# --- Question 2: Find total classroom requirements using unique subjects ---
print("\n--- Classroom Count Practice ---")
subjects_list = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]

# Logic: Passing the list into a set automatically dedupes it. 
# The size of the set tells us exactly how many unique classes exist.
unique_subjects = set(subjects_list)
print("Unique subjects offered:", unique_subjects)
print(f"Total classrooms needed: {len(unique_subjects)}")


# --- Question 3: Accept 3 user-inputted subject grades into an empty dictionary ---
print("\n--- User Marks Dictionary Practice ---")
marks_dict = {}

# Prompting the user and building the key-value pairs sequentially
sub1 = input("Enter 1st subject name: ")
score1 = float(input(f"Enter marks for {sub1}: "))
marks_dict[sub1] = score1

sub2 = input("Enter 2nd subject name: ")
score2 = float(input(f"Enter marks for {sub2}: "))
marks_dict[sub2] = score2

sub3 = input("Enter 3rd subject name: ")
score3 = float(input(f"Enter marks for {sub3}: "))
marks_dict[sub3] = score3

print("Collected marks record:", marks_dict)


# --- Question 4: Figure out a way to store 9 & 9.0 as separate values in a set ---
print("\n--- Unique Values in Set Practice ---")
# Context: Normally Python evaluates 9 == 9.0 as True, so a set strips one away.
normal_set = {9, 9.0}
print("Standard set behavior (collapses them):", normal_set)

# Trick Solution: Store one of the values as a different data type, like a string!
clever_set = {9, "9.0"}
print("Using string typecasting solution:", clever_set)

# Alternate Solution: Store them as explicit key-value-like tuples to trick the float evaluator
tuple_set = {(9, "int"), (9.0, "float")}
print("Using tuple tracking solution:", tuple_set)