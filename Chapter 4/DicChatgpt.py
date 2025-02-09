# Creating a dictionary
dict1 = {"name": "Alice", "age": 25, "city": "New York"}

# Dictionary Methods
print(dict1.keys())             # Output: dict_keys(['name', 'age', 'city'])
print(dict1.values())           # Output: dict_values(['Alice', 25, 'New York'])
print(dict1.items())            # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])
print(dict1.get("age"))         # Output: 25
print(dict1.get("country", "USA"))  # Output: USA

dict1.update({"age": 26})       # Update value
print(dict1)                    # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

dict1.pop("city")               # Remove a key
print(dict1)                    # Output: {'name': 'Alice', 'age': 26}

dict1.setdefault("gender", "Female")  # Add new key with default value
print(dict1)                    # Output: {'name': 'Alice', 'age': 26, 'gender': 'Female'}

# Copying a dictionary
dict2 = dict1.copy()
print(dict2)                    # Output: {'name': 'Alice', 'age': 26, 'gender': 'Female'}

# Clearing a dictionary
dict2.clear()
print(dict2)                    # Output: {}

# Creating a dictionary from keys
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(default_dict)              # Output: {'a': 0, 'b': 0, 'c': 0}

# Checking key existence
print("name" in dict1)           # Output: True

# Iterating through a dictionary
for key, value in dict1.items():
    print(key, ":", value)

# Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)                   # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
