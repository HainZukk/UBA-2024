def calculo():
    num1=int(input("ingrese un numero entero : "))
    num2=int(input("ingrese el segundo numero entero : "))

    suma= num1 + num2
    resta= num1 - num2
    multi= num1 * num2 
    division= num1 / num2
    resto= num1 // num2

    print("Suma : ", suma)
    print ("Resta : " ,resta)
    print("Multiplicacion : " , multi)
    print("Division : ",division)
    print("Resto : " , resto)

calculo()