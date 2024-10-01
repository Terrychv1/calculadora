# funcion sumar

def sumar ( a, b):
    return a + b
def restar ( a, b):
    return a - b

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

print("Calculadora")
print("1. Sumar")

while True:
        opcion = input("Selecciona una opción (1/2/3) o 'salir' para terminar: ")

        if opcion == '1':
            print("Resultado:", sumar(a, b))
        elif opcion == '2':
            print("Resultado:", restar(a, b))
