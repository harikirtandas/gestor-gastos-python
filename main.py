import csv
import os

# Leer gastos desde archivo CSV si existe
gastos = {}

if os.path.exists("gastos.csv"):
    with open("gastos.csv", mode="r", newline="") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if len(fila) == 2:
                categoria, monto = fila
                try:
                    gastos[categoria] = float(monto)
                except ValueError:
                    pass

# main.py
 
def analizar_gastos(gastos):
    total = 0
    print("Gastos:")
    for categoria, monto in gastos.items():
        print(f"{categoria}: ${monto}")
        total += monto
    print(f"\nTotal gastado: ${total}")

    if total > 100000:
        print("⚠️ ¡Cuidado! Superaste tu presupuesto mensual.")
    else:
        print("✅ Bien, estás dentro del presupuesto.")


# Diccionario con gastos de ejemplo
gastos = {
    "alquiler": 75000,
    "comida": 22000,
    "internet": 8000,
    "ropa": 15000
}



# Pedir al usuario que ingrese categorias y montos
while True:
    print('\n--- MENÚ ---')
    print('1. Ingresar gasto.')
    print('2. Salir.')
    opcion = input('\nIngresá una opción: ')
    
    if opcion == '2':
        print('Gracias por usar la app de gastos!')
        break
    elif opcion == '1':
        while True:
            categoria = input('Ingresa la categoría del gasto (o escribí "fin" para volver al menú): ')
            if categoria.lower() == 'fin':
                break
            while True:
                try:
                    monto = float(input(f'Ingresa el monto para {categoria}: '))
                    break
                except ValueError:
                    print('Ingresá un monto válido.')
            gastos[categoria] = monto
            analizar_gastos(gastos)
        
# Llamar a la función
analizar_gastos(gastos)