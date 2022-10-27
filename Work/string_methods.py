"""
Strings have a wide variety of other methods for testing and manipulating the text data. This is a small sample of methods:

"""

s = 'Hello World'
a = 'halloween'
b = '-'

s.endswith('d')     # Check if string ends with suffix
s.find('l')              # First occurrence of t in s
s.index('o')             # First occurrence of t in s
s.isalpha()            # Check if characters are alphabetic
s.isdigit()            # Check if characters are numeric
s.islower()            # Check if characters are lower-case
s.isupper()            # Check if characters are upper-case
b.join(a)          # Join a list of strings using s as delimiter
s.lower()              # Convert to lower case
s.replace('e','8')     # Replace text
s.rfind('e')             # Search for t from end of string
s.rindex('e')            # Search for t from end of string
s.split([delim])       # Split string into list of substrings
s.startswith('b')   # Check if string starts with prefix
s.strip()              # Strip leading/trailing space
s.upper()              # Convert to upper case