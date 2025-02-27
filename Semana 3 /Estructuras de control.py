#Estructuras de control 
#Nos permite controlar el flujo de nuestro codigo 

#Estructuras condicionales 
# -Selectivas
    #Si pasa tal cosa entonces hago esto 


#ejemplo
#llueve = False
#si llueve entonces 
#me abrigo 

#hay_sol = True
#si hay_sol entonces
#uso gorra

#Sintaxis de esta estructura
#if expresion:
   # accion_1
   # accion_2

#ejemplos
hay_sol = True
hace_frio = True
if hay_sol and not hace_frio:                         #if = Si    not = no
    print("Voy a usar gorra y no me pongo buzo")
elif hay_sol and hace_frio:
    print("voy a usar gorra y buzo")
elif not hay_sol and not hace_frio:
    print("Salgo sin gorra y sin buzo")
else:   #Sino                       , si todo lo anbterior da false
    print("Salgo sin gorra y me pongo buzo")



#Esctructuras iterativas
