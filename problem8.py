# write a program to print the following star patter 
# *
# **
# ***

n = int(input("enter a number:"))
for i in range(1,n+1):
    print(" "* (n-1), end="")
    print("*"*(2*i-i), end="")
    print()