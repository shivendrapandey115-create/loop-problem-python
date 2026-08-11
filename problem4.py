# write a program to find whetrher a given number is prime or not 

n = int(input("enter a number :"))
for i in range (2, n):
    if(n%i) == 0:
        print("number is not a prime")
        break