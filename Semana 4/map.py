
def cortar_palabra (palabra):
    return palabra[:4] #[Desde donde , Hasta donde , cada cuanto]

palabras = (
    "perro",
    "mesa",
    "silla",
    "auto",
    "planta",
    "arbol",
    "plata"
)

palabras_cortas = map(cortar_palabra , palabras) 
print(list(palabras_cortas))