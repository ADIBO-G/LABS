#question 1
'''
print('     ',end=" ")
for i in range(1,10):
    print(f'{i:4}',end='  ')
print('-'*60)
print()

for j in range(1,10): 
    print(j,'|',end='   ')
    for i in range(1,10):
        print(f'{i+j:3}',end='   ')
    print()
''' 
#question 2
'''
n=int(input("enter"))
i=0

while i!=999:
    i+=1
    if i%n==0:
        if i%4==0:
            continue
        else:
            print(i,end=" p")
'''  
#question3 
#a
'''
n=int(input("enter:"))
i=0
while i!=n:
    i+=1
    j=0
    while j!=i:
        print(j+1,end=" ")
        j+=1
    print()
'''
#b
'''
n=int((input("enter")))
i=0
while i!=n:
    j=n-i
    while j!=0:
        print('*',end=" ")
        j-=1
    print()
    i+=1
'''
#c
'''
n=int((input("enter")))
i=0
while i!=n:
    j=0
    while j!=2*(n-i)-2:
        j+=1
        print(" ",end="")
        
    j=0
    while j!=i+1:
        j+=1
        print('*',end=" ")
        
    print()
    i+=1
'''
#question4
'''
n=int(input("enter:"))
a=n
oc=0

while a!=0:
    
    oc=(oc*10)+(a%8)
    a=a//8
oc=str(oc)
print("Octal equivalent:",oc[-1::-1])
if n==0:
    print("Octal equivalent:",0)
'''
#question5
'''
n=int(input())
w=0
r=0
i=0
while i<n:
    d=int(input())
    if d>w:
        r=w
        w=d
    if d>r and d<w:
        r=d
    
    i+=1
print(w)
print(r)
'''
#question6
'''
n=int(input())
for i in range(2,n):
    a=i
    s=0
    while a!=0:
        s=s+((a%10)**3)
        a=a//10
        
    if s==i:
        print(i)
'''
#question 7
'''
print(f"{'N':<5}{'N^2':<7}{'N^3':<8}{'Square Root':<10}")

for i in range(1,16):
    print(f"{i:<5}{i**2:<7}{i**3:<8}{i**(1/2):.4f}")
'''   

#question 8
'''
n=int(input("enter number of lines"))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print(i,end=" ")
    print()
'''
#question 9 
n=int(input("enter number"))
a=1
for i in range(n):
    for j in range(i+1):
        print(a,end=" ")
        a+=1
    print()
#question 10
'''
n=int(input("enter:"))
for i in range(n):
    if i<=n//2:
        for j in range((n//2)-i):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        print()

    else:
        for j in range(i-(n//2)):
            print(" ",end=" ")
        for j in range(2*(n-i)-1):
            print("*",end=" ")
        print()
   '''







#hollow rhombus
"""
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(n):
        if i==0 or i==n-1:
            print("*",end=" ")
        elif j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
            """





































        
        
        
        
        
        
        
        

































