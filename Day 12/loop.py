'''
pin = 9618
for i in range(5):
    epin = int(input("Enter pin: "))
    if epin == pin:
        print("unlock phone")
        break
    else:
        print("incorrect pin")
else:
    print("Try after 60 seconds")'''
n = int(input("Enter number: "))
for i in range (2,n//2+1):
    if n%i==0:
        print("prime number")
        break
else:
    print("Not a prime number")

for i in range (2,n//2+1):
    if n%2==0:
        print("prime number")
        break
else:
    print("Not a prime number")