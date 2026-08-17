
#<1>
'''x1,y1=map(int,input().split())
r=int(input("Enter the radius r:"))
x2,y2=map(int,input().split())
if ((x2-x1)**2)+((y2-y1)**2) ==r**2 :
    print("On the boundary")
elif ((x2-x1)**2)+((y2-y1)**2)>r**2 :
    print("Outside the circle")
elif ((x2-x1)**2)+((y2-y1)**2)<r**2 :
    print("Inside the circle")'''


#<2>
'''s=int(input())
Area=float((5*s**2)/0.73)
print("Area: ",Area)'''

  
#<3>
'''A,B,C=map(int,input().split())
if A+B+C==180:
    print("Angles can make a triangle")
    if A>60 and B>60 and C>60 :
        print("Obtuse triangle")
    elif A<60 and B<60 and C<60 :
        print("Acute triangle")
    else:
        print("Equilateral triangle")
else:
    print("Not an triangle")'''
    
    
#<4>
'''x=input()
if 1000<=int(x)<=9999:
    Sum1=int(x[0])+int(x[1])
    Sum2=int(x[2])+int(x[3])
    print(Sum1)
    print(Sum2)
    if Sum1==Sum2:
        print("equal")
    elif Sum1>Sum2:
        print("1st sum is greater than 2nd sum")
    else:
        print("2nd sum is greater than 1st year")

else:
    print("Invalid Input")'''
    
    
#<5>
'''x = input()
if 10000 <= int(x) <= 99999:
    x0 = int(x[0])
    x1 = int(x[1])
    x2 = int(x[2])
    x3 = int(x[3])
    x4 = int(x[4])

    if x0>=x1 and x0>=x2 and x0>=x3 and x0>=x4:
        largest=x0
        position ="1st"
    elif x1>=x2 and x1>=x3 and x1>=x4:
        largest=x1
        position ="2nd"
    elif x2>=x3 and x2>=x4:
        largest = x2
        position ="3rd"
    elif x3>=x4:
        largest=x3
        position ="4th"
    else:
        largest=x4
        position="5th"

    print(largest)
    print(position)
else:
    print("Invalid Input")'''
    
#<6>
'''a = 999
b = 777
c = 666
a = a + b + c  # a now holds the total sum (A + B + C)
b = a - b - c  # b gets (A + B + C) - B - C = A
c = a - b - c  # c gets (A + B + C) - A - C = B
a = a - b - c  # a gets (A + B + C) - A - B = C

print(f"a = {a}, b = {b}, c = {c}")'''

#<7>
'''x=input()
x0=int(x[0])
x1=int(x[1])
x2=int(x[2])
sumx=x0+x1+x2
if (int(x))%sumx==0:
    print("Not harshad's Number")
else:
    print("Harshad's Number")'''
    

#<8>
'''v=int(input())
n=int(input())
vn=v*0.95**n+((1-0.95**n)/0.05)*10
if v>5 and n>0:
    print(f'Volume on {n} day is {vn:.2f} litres')

else:
    print(f'Invalid input')'''




#<9>
'''a1,b1,c1,a2,b2,c2=map(int,input().split())


if a1==b1==0 or a2==b2==0: 
    print("Invalid input")

elif a1/a2==b1/b2==c1/c2:
    if a1/a2==b1/b2==c1/c2==1:
        print("Coincident Lines")
    
    else:
        print("Parallel Lines")
else:
    x=(b1*c2-b2*c1)/(a1*b2-a2*b1)
    y=(c1*a2-c2*a1)/(a1*b2-a2*b1)
    print(f'Point of intersection is {x:.2f},{y:.2f}')'''
    



        
