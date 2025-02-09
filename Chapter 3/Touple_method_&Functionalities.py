# Creating a tuple
tup = (1, 2, 3, 2, 2, 4, 5)

# Tuple Methods
print(tup.count(2))          # Output: 3
print(tup.index(3))          # Output: 2

# Built-in Functions
print(len(tup))              # Output: 7
print(max(tup))              # Output: 5
print(min(tup))              # Output: 1
print(sum(tup))              # Output: 19
print(sorted(tup))           # Output: [1, 2, 2, 2, 3, 4, 5]
print(any(tup))              # Output: True
print(all(tup))              # Output: True

# Converting list to tuple
lst = [10, 20, 30]
print(tuple(lst))            # Output: (10, 20, 30)

# Tuple Operations
print((1, 2) + (3, 4))       # Output: (1, 2, 3, 4)
print(("hello",) * 3)        # Output: ('hello', 'hello', 'hello')
print(5 in tup)              # Output: True

# Tuple Unpacking
a, b, c = (10, 20, 30)
print(a, b, c)               # Output: 10 20 30
print(tup.count(3))
print(sum(tup))
