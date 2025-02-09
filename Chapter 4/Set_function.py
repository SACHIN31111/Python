# Adding an element
numbers={1,2,3,4,5,6,6}
numbers.add(6)
print(numbers)  # {1, 2, 3, 4, 5, 6}

# Removing an element (KeyError if not found)
numbers.remove(3)

# Removing an element safely (no error if not found)
numbers.discard(10)  # No error if 10 is missing

# Removing and returning an arbitrary element
removed_item = numbers.pop()
print(removed_item)  # Random element removed

# Clearing all elements
numbers.clear()
