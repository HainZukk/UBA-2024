def calcular_total(ticket):
    total = 0
    for producto in ticket:
        precio_por_unidad = producto["Precio por unidad"]
        cantidad = producto["Cantidad"]
        total += precio_por_unidad * cantidad
    return total

# Ejemplo de uso:
ticket = [
    {"Nombre del producto": "Leche", "Precio por unidad": 2.5, "Cantidad": 2},
    {"Nombre del producto": "Pan", "Precio por unidad": 1.0, "Cantidad": 3},
    {"Nombre del producto": "Huevos", "Precio por unidad": 0.5, "Cantidad": 12}
]

monto_total = calcular_total(ticket)
print("El monto total a pagar es:", monto_total)
