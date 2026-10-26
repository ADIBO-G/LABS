#Lab8
#1
'''
s=input()
v=0
c=0
d=0
sp=0
o=0
for i in s:
    if i.lower() in "aeiou":
        v=v+1
    elif i.isalpha():
        c=c+1
    elif i.isdigit():
        d=d+1
    elif i==" ":
        sp=sp+1
    else:
        o=o+1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("Spaces:",sp)
print("Others:",o)
'''
#2
'''
s=input()
r=""
for i in range(len(s)):
    if i%2==0:
        r=r+s[i].upper()
    else:
        r=r+s[i].lower()
print(r)
#Q3
s=input()
u=0
l=0
d=0
sp=0
for i in s:
    if i.isupper():
        u=1
    elif i.islower():
        l=1
    elif i.isdigit():
        d=1
    elif i!=" ":
        sp=1
t=u+l+d+sp
if len(s)<8:
    print("WEAK")
elif t==4:
    print("STRONG")
elif t>=2:
    print("MODERATE")
else:
    print("WEAK")
'''
#4
'''
s=input()
x=input()
c=0
a=[]
for i in range(len(s)):
    if s[i]==x:
        c=c+1
        a=a+[i]
print("Count:",c)
if c==0:
    print("Positions: -1")
else:
    print("Positions:",*a)
'''
#5
'''
s=input()
a=[]
for i in s.split():
    a=a+[len(i)]
print(*a)
'''
#6
'''
s=input()
flag=1
if len(s)!=10:
    flag=0
else:
    if s[0:2]!="RJ":
        flag=0
    for i in range(10):
        if i in [0,1,4,5]:
            if not(s[i]>="A" and s[i]<="Z"):
                flag=0
        elif not(s[i]>="0" and s[i]<="9"):
            flag=0
if flag==1:
    print(True)
else:
    print(False)
'''
#7
'''
s=input()
c=0
for i in range(len(s)//2):
    if s[i]!=s[len(s)-1-i]:
        c=c+1
print("Changes needed:",c)
#Q8
s=input()
r=""
for i in s:
    if i not in r:
        r=r+i
print(r)
'''
#9
'''
s=input()
k=int(input())
r=""
for i in s:
    if i==" ":
        r=r+" "
    else:
        r=r+chr((ord(i)-97+k)%26+97)
print(r)
'''
#10
'''
s=input()
ch=s[0]
m=1
c=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c=c+1
    else:
        c=1
    if c>m:
        m=c
        ch=s[i]
print(ch,m)
'''
