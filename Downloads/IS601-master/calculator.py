def add():
    return float(input ("Enter a number: ")) + float(input ("Enter another number: "))

def subt():
    return float(input ("Enter a number: ")) - float(input ("Enter another number: "))

def mult():
    return float(input ("Enter a number: ")) * float(input ("Enter another number: "))

def division():
    return float(input ("Enter a number: ")) / float(input ("Enter another number: "))

def square():
    return float(input ("Enter a number: ") )** 2

def sqrt():
    return float(input ("Enter a number: ") )** 0.5


choice = input("press ""1.Add,"
           " 2.subtract,"
          "3.multiply,"
          "4.divide,"
          "5.square,"
          "6.square root")
if  choice == "1":
    print(add ())
elif choice == "2":
    print(subt ())
elif choice == "3":
    print(mult ())
elif choice == "4":
    print(division ())
elif choice == "5":
    print(square ())
elif choice == "6":
    print(sqrt ())
else:
    print ("Enter a valid option")
