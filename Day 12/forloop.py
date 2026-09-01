'''names = {'karthik', 'Tarun'}
for name in names:
    print(name)


d = {1:2,2:3,3:4,4:5,6:7}
for i in d:
    print(i,d[i])

for i in range(1,11,2):
    print(i)

for i in range(10,0,-1):
    print(i)
for n in range(20,0,-2):
    print(n)
s = 'python programming language'
for i in range(len(s)):
    print(i,s[i])

s = [123,23,434,2345,567]
for i in range(len(s)):
    print(i,s[i])
s = [123,345,566,789]
for i in enumerate(s):
    print(i[0],i[1])
for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)

for i in range(1,11):
    if i == 15:
        print(i)
else:
    print('End of loop')
s = [11,12,13,14,15]
n = 12
for i in s:
    if i==n:
        print(n,'found')
        break
else:
    print(i,'not found')
pin = 1234
for i in range(5):
    epin = int(input("Enter the pin: "))
    if epin == pin:
        print("unlock phone")
        break
    else:
        print("Invalid pin")
else:
    print("Try after sometime")'''
n = 18
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a prime number")
        break
else:
    print("Prime number")