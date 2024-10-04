# funcion sumar

def sumar ( a, b):
    c= a + b
    
    return c
def dividir (a,b):
     return a // b

def restar ( a, b):
    return a - b

def multiplicar ( a, b):
    return a * b

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

print("Calculadora")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

while True:
        opcion = input("Selecciona una opción (1/2/3) o 'salir' para terminar: ")

        if opcion == '1':
            print("Resultado:", sumar(a, b))
        elif opcion == '2':
            print("Resultado:", restar(a, b))
        elif opcion == '3':
            print("Resultado:", multiplicar(a, b))
        elif opcion == '4':
             print('Resultado:',dividir(a,b))    
