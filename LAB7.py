#Lab7
#1
'''
s=input()
r=""
for i in s:
    r=i+r
print(r)
'''
#2
'''
s=input()
c=0
i=len(s)-1
while i>=0 and s[i]==" ":
    i=i-1
while i>=0 and s[i]!=" ":
    c=c+1
    i=i-1
print(c)
'''
#3
'''
s=input()
w=input()
if w in s:
    print("Found")
else:
    print("Notfound")
print(s.count(w))
'''
#4
'''
s=input().lower()
check=0
for i in "abcdefghijklmnopqrstuvwxyz":
    if i in s:
        check=1
if check==1:
    print("Pangram")
else:
    print("Not a pangram")
'''
#Q5
s=input()
k=int(input())
r=""
for i in s:
    if i>="a" and i<="z":
        r=r+chr((ord(i)-97+k)%26+97)
    else:
        r=r+chr((ord(i)-65+k)%26+65)
print(r)
#Q6
print("enter1to10,-1tostop")
a=[0,0,0,0,0]
n=0
x=int(input())
while x!=-1:
    if x>=1 and x<=10:
        a[(x-1)//2]=a[(x-1)//2]+1
        n=n+1
    x=int(input())
t=["1 - 2","3 - 4","5 - 6","7 - 8","9 - 10"]
for i in range(5):
    if n>0:
        p=a[i]/n*100
    else:
        p=0
    st=t[i]+": "
    for j in range(int(p/5+0.5)):
        st=st+"# "
    print(st+"{:.2f} %".format(p))
#7
'''
s=input()
i=0
j=len(s)-1
check=1
while i<len(s)-1:
    if s[i]!=s[j]:
        check=0
        break
    i=i+1
    j=j-1
if check==1:
    print("Palindrome")
else:
    print("Not a palindrome")
'''
#8
'''
n=int(input())
l=[]
for i in range(n):
    l=l+[int(input())]
s=0
p=1
smallest=l[0]
for i in l:
    s=s+i
    p=p*i
    if i<smallest:
        smallest=i
print(s)
print(p)
print(smallest)
'''
#9
'''
n=int(input())
l=[]
for i in range(n):
    l=l+[int(input())]
for i in range(len(l)):
    for j in range(len(l)-1-i):
        if l[j]<l[j+1]:
            smallest=l[j]
            l[j]=l[j+1]
            l[j+1]=smallest
print(l)
'''
#10
'''
s=input()
l=s.split("-")
for i in range(len(l)):
    for j in range(len(l)-1-i):
        if l[j]>l[j+1]:
            largest=l[j]
            l[j]=l[j+1]
            l[j+1]=largest
r=""
for i in range(len(l)):
    r=r+l[i]
    if i!=len(l)-1:
        r=r+"-"
print(r)
'''
#11
'''
s=input()
d=0
a=0
u=0
l=0
sp=0
for i in s:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        a=a+1
        if i.isupper():
            u=u+1
        else:
            l=l+1
    else:
        sp=sp+1
print("Digits:",d)
print("Alphabets:",a)
print("Uppercase:",u)
print("Lowercase:",l)
print("Special:",sp)
'''
#12
'''
s=input()
r=""
for i in s:
    if i not in r:
        r=r+i
print(r)
'''
