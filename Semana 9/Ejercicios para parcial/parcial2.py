def entPositivo(cartel):
    pedir = True
    while pedir:
        try:
            n = int(input(cartel))
            if n > 0:
                pedir = False
            else:
                print('Tiene que ser mayor que 0')
        except ValueError:
            print('Número entero')
    return n
  
