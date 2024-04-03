#!/usr/bin/python3

name = "\tblack\that\thacker\n"

name2 = "\trules\n"

print(f"{name.rstrip()} {name2.rstrip()}")
print(f"{name.lstrip()} {name2.lstrip()}")
print(f"{name.strip()} {name2.strip()}")

name = name.strip()
name2 = name2.strip()

print(f"{name} {name2}")

