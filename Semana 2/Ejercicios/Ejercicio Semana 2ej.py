nomMen=input("Quien?")
edadMen=int(input(f"Ingrese la edad de {nomMen} "))


nomMayor = input(f"Como se llama el hermano mayor de {nomMen}? : ")
diferen = int(input(f"Cuantos años mas tiene {nomMayor} : "))

edadMayor= edadMen+diferen
print(nomMen,"Tiene", edadMen , "años ")
print(nomMayor , "es mayor y tiene" , edadMayor, "años ")