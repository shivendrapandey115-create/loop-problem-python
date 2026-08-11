# write a program to greet all the person name stored in a list
# "l" and which start with s
l = ["rudra", "prince", "nitin", "shivendra"]


for item in l:
    if(item.startswith("s")):
        print(f"namaste {item}")
