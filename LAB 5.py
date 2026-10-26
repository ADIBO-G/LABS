#   QUESTION1
'''
x=int(input("first:"))
y=int(input("second:"))
n=int(input("divisior:"))
a=0
if 1<=x<=10000 and 1<=y<=10000 and 1<=n<=100:
    for i in range(x,y+1):
        if i%n==0:
            print(i)
            a+=1
        
print(f'Number of polls are {a}')
'''

#   QUESTION2
'''
n=int(input("Enter number:"))

b=1
while n!=0:
    b=b*(n%10)
    n=n//10
print(b)
'''

#   QUESTION3
'''
n=int(input("Enter number:"))
i=0
count=0
while i!=-999:
    count=count+i
    i=int(input("Enter amount"))
print(count)
if count>n:
    print("Large bill")
else:
    print("Small bill")
'''


#   QUESTION 4
'''
n=int(input("Enter base:"))
p=int(input("Enter power:"))
i=0
r=1
while i<p:
    r=r*n
    i+=1

print(f'N to the power P is equal to {r}')
'''
#   QUESTION 5
'''
a=int(input("first number:"))
b=int(input("second number:"))
c=0
while a!=0:
    c=c*10+a%10
    a=a//10
print(c)
if c==b:
    print("B IS REVERSE OF A")
else:
    print("B is not reverse of a")
'''


#   QUESTION 6
'''
n=int(input("Enter number of terms"))
r=1

for _ in range(n):
    r=r*2
    print(r)
'''

#   QUESTION 7
'''
n=int(input("Enter number"))
sd=0
for i in range(1,n):
    if n%i==0:
        sd+=i
if sd==n:
    print("it is a perfect number")
else:
    print("it is not a perfect number")

'''

#   QUESTION 8
'''
n=int(input("enter number:"))
a="*"
for i in range (n):
    print(a*(i+1))
'''
#   QUESTION 9
'''
n=int(input("Enter number:"))
d=int(input("Enter digit:"))
count=0
while n!=0:
    if n%10==d:
        count+=1
    n=n//10
print(count)
'''

#   QUESTION10
'''
n=int(input("Enter number:"))
count=2

for i in range(2,n):
    if n%i==0:
        count+=1
        print(i)
print(n)
print(f'Number of divisors is {count}')  
if count==2:
    print("Number is prime")
else:
    print("Number is not prime")
'''














