# String Function
name ="rAMALINGAREDDY"
print(len(name))   #length
print(name.endswith("DDY"))
print(name.startswith("RAMA"))
print(name.capitalize())
print(name.find("D"))
print(f"'{name}'")  # This will show if there are extra spaces.
print(name.count("D"))
print(name.replace("D","Z"))


# 1. Length & Searching
# len(s) → Returns the length of the string.
# s.startswith(substring) → Checks if the string starts with the given substring.
# s.endswith(substring) → Checks if the string ends with the given substring.
# s.find(substring) → Returns the index of the first occurrence of the substring, or -1 if not found.
# s.rfind(substring) → Returns the index of the last occurrence of the substring.
# s.count(substring) → Returns the number of occurrences of a substring.
# 2. Modification & Formatting

# s.upper() → Converts the string to uppercase.
# s.lower() → Converts the string to lowercase.
# s.title() → Converts the first character of each word to uppercase.
# s.capitalize() → Capitalizes the first character of the string.
# s.strip() → Removes leading and trailing spaces.
# s.lstrip() → Removes leading spaces.
# s.rstrip() → Removes trailing spaces.
# s.replace(old, new) → Replaces occurrences of old with new.
# s.split(separator) → Splits the string into a list based on the separator.
# s.join(iterable) → Joins elements of an iterable into a single string using s as the separator.
# 3. Checking Content

# s.isalpha() → Returns True if all characters are letters.
# s.isdigit() → Returns True if all characters are digits.
# s.isalnum() → Returns True if all characters are alphanumeric (letters and numbers).
# s.isspace() → Returns True if the string consists of only whitespace characters.
# s.islower() → Returns True if all characters are lowercase.
# s.isupper() → Returns True if all characters are uppercase.
# s.istitle() → Returns True if the string is title-cased.
# 4. String Alignment

# s.center(width, char) → Centers the string using char as padding.
# s.ljust(width, char) → Left-aligns the string using char as padding.
# s.rjust(width, char) → Right-aligns the string using char as padding.
# s.zfill(width) → Adds leading zeros to make the string width characters long.
# 5. Encoding & Decoding
# s.encode(encoding) → Encodes the string into bytes.
# s.decode(encoding) → Decodes bytes into a string.
# Would you like examples for any specific function? 😊🚀