#!/usr/bin/python3

# simple print
message_1 = "Hello h4ck3r"
print(message_1)

# add a new variable
message_2 = "Hacking is the most valuable skill"
print(message_2)

# use double and single quotes
quotes = "pyhton is a hacker's language"
print(quotes)

#add a newline with \n
line_1 = "this is the 1st line\n"
line_2 = "this is the 2nd line"
print(line_1)
print(line_2)

# Changing Case in a String with Methods
name = "aDa lOvELace"

print(name.title())
print(name.upper())
print(name.lower())

# Using Variables in f-Strings (format strings)
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(full_name)
print(f"Hello, {full_name.title()} you are going to be become a hacker!")

# You can also use f-strings to compose a message, and then assign the
# entire message to a Variables
message_3 = f"Hello, {full_name.title()}"
print(message_3)

# Adding Whitespace to Strings with Tabs or Newlines
# To add a tab to your text, use the character combination \t

print("Python")
print("\tPython")

# To add a newline in a string, use the character combination \n
print("Languages:\nPython\nC\nJavascript")


# combine tabs and newlines in a single string.
print("Languages:\n\tPython\n\tC\n\tJavascript")

# Stripping Whitespace
fav_laguage = " Python "
print(fav_laguage.rstrip()) #removes whitespace to the right
print(fav_laguage.lstrip()) #removes whitespae to the left
print(fav_laguage.strip()) #removes whitespace to both side

# To remove the whitespace from the string permanently, you have to
# associate the stripped value with the variable name
fav_laguage = fav_laguage.strip()
print(fav_laguage)


# Removing Prefixes & Suffix
hfp_url = "https://hfpsecurity.com"
print(hfp_url)
print(hfp_url.removeprefix("https://"))
print(hfp_url.removesuffix(".com"))

# A list is a collection of items in a particular order. lists start at 0
bicycles = ["trek", "dolan", "specialized","redline"]
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[3])
print(bicycles[1].title())
print(bicycles[-1])

print(f"My first track bike was a {bicycles[1].title()}")

# Modifying Elements in a List
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

# Inserting Elements into a List
motorcycles.append("honda")
print(motorcycles)

motorcycles.insert(0, "firestone")
print(motorcycles)

motorcycles.insert(2, "hackstone")
print(motorcycles)

# Removing Elements from a List
print(motorcycles)
del motorcycles[2] #deletes hackstone from the list
print(motorcycles)

# Removing an Item Using the pop() Method
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned}.")

# Removing an Item by Value
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

too_expensive = "suzuki"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# Sorting a List Permanently with the sort() Method
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

# reverse-alphabetical order
cars.sort(reverse=True)
print(cars)


# Sorting a List Temporarily with the sorted() Function
cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("Here is the original list:")
print(cars)

# Printing a List in Reverse Order
cars.reverse()
print(cars)

# Finding the Length of a List - Python counts the items in a list starting with one, so you shouldn’t run into any
#off-by-one errors when determining the length of a list
cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars))

