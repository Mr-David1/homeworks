from fractions import Fraction
operation=input("start")
print("choose one option: ")
print("1.SUM")
print("2.MULTYPLY")
print("3.DIFFERENCE")
print("4.DEVISION")
operation=input ()

if operation=="1":
 x=Fraction(input("first variable: "))
 y=Fraction(input("second variable: "))
 z=Fraction(input("third variable: "))
 
 print("the sum is: " + str( x + y + z ))
elif operation=="2":
 x=Fraction(input("first variable: "))
 y=Fraction(input("second variable: "))
 z=Fraction(input("third variable: "))
 print("the multyply is: " + str( x * y * z ))
elif operation=="3":
 x=Fraction(input("first variable: "))
 y=Fraction(input("second variable: "))
 z=Fraction(input("third variable: "))
 print("the difFerence is: " + str( x - y - z ))
elif operation=="4":
 x=Fraction(input("first variable: "))
 y=Fraction(input("second variable: "))
 z=Fraction(input("third variable: "))
 print("the devision is: " + str( x / y / z ))
else:
      print("invalid entry!")
 
 
operation=input('start')
temp=str(input("what is your name?: "))
age=int(input("what is your age?:"))
height=float(input("what is your height?: "))
place=str(input(" where do you live?: "))
identify=str(input("are you a humen?: "))
(if name== str ("dato")and age==20 and height==187 and place==str("signagi") and identify==("yes"):)

print("everithing is ok! ")
print("go outside! ")
else:
print("wrong person! ")
print("stay inside! ")
