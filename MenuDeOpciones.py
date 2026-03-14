print(" Menu de opciones:")
print('1.                 Sumar')
print('2.                 Restar')
print('3.                 Multiplicar')
print('4.                 Dividir0')

opcion = int(input("Elija una opcion (1-4):    "))
numb1 = float(input("Ingrese el primer numero:"))
numb2 = float(input("Ingrese el segundo numero:"))

if opcion == 1: 
    print("Resultado:", numb1  + numb2)
elif opcion == 2:  
    print("Resultado:", numb1 - numb2)
elif opcion == 3:  
     print("Resultado:", numb1 * numb2)
elif opcion == 4:  
    print("Resultado:", numb1 != 0)
    if numb2 !=  0: 
        print("Resultado:", numb1 / numb2)
    else: 
        print("No se puede dividir entre 0") 
else: 
    print("Opcion    Invalida")