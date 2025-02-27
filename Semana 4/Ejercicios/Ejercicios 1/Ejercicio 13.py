# Parte a: Función para calcular el total de un solo ticket
def calcular_total(ticket):
    total = 0
    for producto, precio in ticket:
        total += precio
    return total

# Parte b: Función para juntar dos tickets y calcular el total
def fusionar_tickets(ticket1, ticket2):
    ticket_fusionado = ticket1 + ticket2
    total_fusionado = calcular_total(ticket_fusionado)
    return total_fusionado

# Ejemplo de uso
ticket1 = [("Leche", 2.50), ("Pan", 1.20), ("Manzanas", 3.00)]
ticket2 = [("Queso", 4.50), ("Huevos", 2.00), ("Papel higiénico", 1.80)]

total_ticket1 = calcular_total(ticket1)
print("Total del ticket 1:", total_ticket1)

total_ticket2 = calcular_total(ticket2)
print("Total del ticket 2:", total_ticket2)

total_fusionado = fusionar_tickets(ticket1, ticket2)
print("Total fusionado de ambos tickets:", total_fusionado)
