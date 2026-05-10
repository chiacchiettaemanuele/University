numero = float(input("enter first number : "))
operation=input("press +,-,*,/")
numero2 = float(input("enter  second number : "))

if operation == "+":
    print(numero + numero2)
elif operation == "-":
    print(numero - numero2)
elif operation == "*":
    print(numero * numero2)
elif operation == "/":
    if numero2 != 0:
     print(numero / numero2)
    else:
      print ( "error:division by zero")
else:
 print("invalid operation")
