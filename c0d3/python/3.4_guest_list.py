#!/usr/bin/python3

guest = ["hendrix", "hacker", "mr. robot", "neo"]

print(f"Dear {guest[0]}, you have been invited to dinner at 7pm")
print(f"Dear {guest[1]}, you have been invited to dinner at 7pm")
print(f"Dear {guest[2]}, you have been invited to dinner at 7pm")
print(f"Dear {guest[3]}, you have been invited to dinner at 7pm")

unavailable = "neo"
guest.remove(unavailable)
print(guest)

guest.insert(2, "morpheus")
print(guest)

guest[3] = "nancy"
print(guest)

guest.insert(0, "neo")
guest.insert(3, "jake")
guest.insert(-1, "warren")
print(guest)


print(f"Dear {guest[0].title()}, you have been invited to dinner at 7pm")
print(f"Dear {guest[1].title()}, you have been invited to dinner at 7pm")
print(f"Dear {guest[2].title()}, you have been invited to dinner at 7pm")
print(f"Dear {guest[3].title()}, you have been invited to dinner at 7pm")
print(f"Dear {guest[4].title()}, you have been invited to dinner at 7pm")
print(f"Dear {guest[5].title()}, you have been invited to dinner at 7pm")
print(f"Dear {guest[6].title()}, you have been invited to dinner at 7pm")


popped_list = guest.pop()
print(guest)
print(popped_list)

one_less = guest.pop(0)
print(f"Apologies there is not enough room for you {one_less}")
print(guest)


one_less = guest.pop(1)
print(f"Apologies there is not enough room for you {one_less}")
print(guest)


one_less = guest.pop(2)
print(f"Apologies there is not enough room for you {one_less}")
print(guest)


one_less = guest.pop(0)
print(f"Apologies there is not enough room for you {one_less}")
print(guest)


one_less = guest.pop(1)
print(f"Apologies there is not enough room for you {one_less}")
print(guest)


del guest[0]
print(guest)
