#Lab2
#<1>
#num=int(input("enter a number"))
#if num%5==0:
   # print("Hii")
#else:
   # print("Bye")
   
   
#<2>
#x=float(input("enter length of first parallel side"))  
#y=float(input("enter length of second parallel side"))
'''h=float(input("enter height "))
area=((x+y)/2)*h
print("area of trapezoid =",area,"square metres")'''


#<3>
'''w=float(input("enter weight of in kgs"))
h=float(input("enter height in metres"))
bmi=w/(h**2)
print("your BMI is :",bmi)
if bmi<18.5:
    print("you are underweight")
elif bmi<25:
    print("you are normal")
elif bmi<30:
    print("slightly overweight")
elif bmi<35:
    print("you are obese")
else:
    print("you are clinically obese")'''
    
#<4>
'''alphabet=str(input("enter your alphabet"))
if alphabet in"aeiouAEIOU":
 print("vowel")
else:
     print("consonant")'''
     
    
#<5>
'''initial=2.19*10**14
final=4.68*10**14
growth=((final-initial)/initial)*100
print( int(growth) ,"%")'''


#<6>
'''months=int(input("enter number of months"))
years=months//12
remainingmonths=months%12
print("years :",years)
print("months :",remainingmonths)'''


#<7>
'''c=input("enter color Blue or Red:")
m=input("enter mode steady or flashing:")
if c=="blue" and m=="steady":
    print("clear view")
elif c=="blue" and m=="flashing":
    print("clouds due")
elif c=="red"and m=="steady":
    print("rain ahead")
elif c=="red" and m=="flashing":
    print("snow instead")
else:
    print("invalid input")'''
    
    
#<8>
'''costs=float(input("enter cost"))
revenue=float(input("enter revenue"))
if costs==revenue:
    print("break even")
elif revenue>costs:
    profit=revenue-costs
    print("profit=",profit)
else:
    loss=costs-revenue
    print("loss=",loss)'''
    

#<9>
'''w=int(input("enter the number of widgets"))
b=w*25
c=w*20
if w<100:
    print("total cost is :",b,'cents')
elif w>=100:
    print("total cost is :",c,"cents")'''


#<10>
'''a=float(input("enter the num of pounds"))
b=float(input("enter the amt in cash"))
c=a*2.50
d=b-c
e=c-b
if d>0:
    print("change from the transaction is:",d)
elif a>0:
    print("you owe $%.2f"% e,"more.")'''


#<11>
a=int(input("enter first num"))
b=int(input("enter second num"))
c=int(input('enter third num'))
if a>b:
    if a>c:
        print("a is the greatest")
    else:
        print("c is the greatest")
elif b>c:
    print("b is the greatest")
else:
    print("invalid")
    

#<12>
'''a=int(input("enter the basic salary"))
HRA=20/100*a
TA=5/100*a
DA=10/100*a
gross=a+HRA+TA+DA
print("gross salary is",gross)'''


#<13>
'''a=int(input("enter basic salary"))
HRA=20/100*a
TA=5/100*a
DA=10/100*a
gross=a+HRA+TA+DA
print("gross salary is",gross)
if gross>300000:
    print("income tax=0% of gross salary")
elif 300000<=gross<1000000:
    print("income tax=10% of gross salary")
elif 1000000<=gross<2500000:
    print("income tax=20% of gross salary")
elif gross<2500000:
    print("income tax=30% of gross salary")
else:
    print("invalid input")'''
    
#<14>
'''a=int(input("enter the income of person"))
b=0.02*a
c=a-20000
d=400+0.025*c
e=a-50000
f=1150+0.035*e
if a<=20000:
    print("income tax of gross salary",b)
elif 20000<a<=50000:
    print("income tax of gross salary",d)
elif a>50000:
    print("income tax of gross salary",f)
else:
    print("invalid input")'''
    


