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

# Función para analizar gastos
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


# Menú de usuario
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
            
            # Guardar en el archivo CSV
            with open("gastos.csv", mode="a", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow([categoria, monto])
                
            analizar_gastos(gastos)
        
# Informe final
analizar_gastos(gastos)