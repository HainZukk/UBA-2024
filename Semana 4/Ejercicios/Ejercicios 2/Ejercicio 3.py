def eliminar_substring(string,substring):
    return string.replace(substring , "")

#Ejemplo de uso 
texto = "Campeones del Mundo - 2022"
substring = "2022"
texto_sin_substring = eliminar_substring(texto , substring)
print(texto_sin_substring)