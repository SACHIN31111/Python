# About Dictionary in Python 📝
# A dictionary in Python is an unordered, mutable collection of key-value pairs. It allows fast lookups, modifications, and deletions.

# Key Features of a Dictionary
# Keys are unique (cannot have duplicate keys).
# Values can be of any data type (int, string, list, tuple, etc.).
# Dictionaries are mutable (modifiable after creation).
# Keys must be immutable (strings, numbers, or tuples).

dic={ "a":"sachin","c":45,"d":False}
print(dic)
dic.update({"a":"sahana"})
print(dic)
print(dic.items())
print(dic.get("a"),dic.keys(),dic.values())

dic.clear()
print(dic)

