#Tipos de operadores
# -Aritmeticos --> = , - , * / Nos permite hacer funciones entre valores
# -Relacionales --> == , != , < , > , <= >= Nos devuelve veradero falso si se cumple o no una relacion.
# -Logicos  --> Nos permite unir otros operadores para formar operaciones mas grandes. and(y) , or(o) , not(no)


#Expresion 
# Valor que devuelve un conjunto de operaciones
      #muchas operaciones relacionales enganchadas a los logicos
#Un conjunto de operaciones que tienen un valor de verdad.


numero_1 = 12
numero_2 = 4
numero_3 = 35
numero_4 = 17
numero_5 = 65

#expresion 1)
(numero_1 > numero_2) --> True

#expresion 2)
(numero_2 == numero_3) --> False

#expresion 3)
(numero_2 < numero_4) and (numero_3 == numero_5) --> 
       True          and           False
--> False         #Para que sea verdadera tienen que ser verdaderas ambas.

e#xpresion 4)
(numero_1 + numero_5 == numero_2) or (numero_3 >= numero_4)
           False                  or          False
---> False

#Asi podemos concatenar todo .
#Buena practica poner parentesis.
