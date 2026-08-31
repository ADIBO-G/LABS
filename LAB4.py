#<1>
'''
x=int(input("Salary: "))
y=int(input("Years of service: "))
if x>5 :
    b=5
else:
    b=0
Totalsalary=x+(x*5/100)
print(Totalsalary)
'''

#<2>
'''
x=input("Password: ")
if x=="s3cr3t!P@ssw0rd":
    print("Welcome")
else:
    print("Wrong password")
'''

#<3>
'''
x=input("Enter shape: ")
if x.lower()=="square" :
    s=int(input("Length of its side"))
    Area=s*s
elif x.lower=="rectangle" :
    side1=int(input("length: "))
    side2=int(input("Breadth"))
    Area=side1*side2
elif x.lower=="circle" :
    r=int(input("Radius: "))
    Area=float(3.14*r*r)
elif x.lower=="Triangle" :
    b=int(input("Base: "))
    h=int(input("Height: "))
    Area=float(0.5*b*h)
print("Area: ",Area)
'''

#<4>
'''
h=int(input("enter hours"))
m=int(input("enter minutes"))

nm=m+15

if nm>59:
    h=h+1
    nm=nm-60
    if h>23:
        h=h-24
       
print(f"{h}:{nm}")
'''



#<5>
'''
n=float(input("Enter kilometres: "))
d=input("Enter day or night: ")
if n<20:
    sf=33.54
    if d.lower=="day" :
        dr=37.89
    else:
        dr=43.17
    price=float(sf+dr*n)
elif n<100:
    dr=4.32
    price=float(dr*n)
elif n>100:
    dr=2.88
    price=float(dr*n)
print("Price: :",price)
'''

#<6>
'''
x=int(input("Enter no. of holidays: "))
hdt=(127*x)
wdt=(365-x)*63
diff=(30000-hdt-wdt)
print("The difference from the norm: ",diff, "minutes per year.")
'''

#<7>
'''
bgn=float(input("Enter BGN: "))
season=input("Season: ")
if bgn<=100:
    print("Bulgaria")
    if season.lower=="summer":
        price=(bgn-bgn*30/100)
    elif season.lower=="winter":
        price=(bgn-bgn*70/100)
elif bgn<=1000:
    print("Balkans")
    if season.lower=="summer":
        price=(bgn-bgn*40/100)
    elif season.lower=="winter":
        price=(bgn-bgn*80/100)
elif bgn<=1000:
    print("Europe")
    if season.lower=="summer":
        price=(bgn-bgn*90/100)
    elif season.lower=="winter":
        price=(bgn-bgn*90/100)
amt=(bgn+price)
print("Total amount: ",amt)
'''

#<8>
'''
for x in range(1,1000):
    if x==6:
        break
    print(x)
'''

#<9>
'''
n = int(input())
total = sum(int(input())
for _ in range(n))
print("The sum is:", total)
'''


#<10>
'''
n=int(input())
for i in range(1,11):
    print(i,"x",n,"=",i*n,"\n")'''

    

    
   
 
 
    
    
