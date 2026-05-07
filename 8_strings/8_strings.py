# raw string --> ignores ALL escape characters --> good for text with backslashes
print(r"The file is in C:\users\alice\desktop")

# multiline string

multi = """
This is a multi line string

I do not need to escape or insert any newline characters

quotations (' and ") are also automatically escaped.
"""

print(multi)

# string slicing:
hello = "Hello world!"
part1 = hello[:6]
part2 = hello[6:-1]

# Slices DO NOT modify the string in place. They return new values

print(hello)
print(part1)
print(part2)

# IN and NOT

print("Hello" in hello)  # True
print("world!.." in hello)  # False

# f-strings --> string literals in JS
value1 = 1230
value2 = 1200
print(f"{hello} was a string that was used in an f-string.")
print(f"{value1} - {value2} is equal to {value1 - value2}")

# ---

# joining strings --> .join()
# method joins an array of strings together using an inbetween character

ats = ["cats", "rats", "bats"]
ats_string = "|".join(ats)
print(ats_string)

# splitting strings --> .split()
# method splits a string into an array --> split is determined by a character
# commonly used with newline characters --> splits it into individual paragraphs / sentences

ats_split = ats_string.split("|")
splitstring = "1 2 3 4 5 6789"
split2 = splitstring.split(" ")
print(ats_split)
print(split2)
