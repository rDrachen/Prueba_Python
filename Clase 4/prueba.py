def entrada():
    menu=int(input("Seleccione una opción: "))
    return

lista="""1-Suma
2-Resta
3-División
4-Multiplicación
5-Tablas de multiplicar
6-Comparasión de 3 números
7-IVA
8-Salir
"""

print(lista)
entrada()
men=menu

while men<8:

    if men in range(1,5):
        a=int (input("Ingrese un número: "))
        b=int (input("Ingrese otro número: "))
        c=int (input("Ingrese un último número: "))
        if men==1:
                print("La suma es: ",a+b+c)
                entrada()
        elif men==2:
                print("La resta es: ",a-b-c)
        elif men==3:
                print("La división es: ",a/b/c)
        elif men==4:
                print("La multiplicación es: ",a*b*c)

    elif men==5:
        a=int(input("Qué tabla desea conocer: "))
        b=int(input("Cúal sería el último multiplicador: "))
        for var in range(1,b+1):
                print(var," x ",a,"= ",var*a)

    elif men==6:
        a=int(input("Ingresa un número: "))
        b=int(input("Ingresa un segúndo número: "))
        c=int(input("Ingresa un último número: "))
        if a==b and b==c and c==a:
                print(a,", ",b," y ",c," son iguales")
        else:
                print(a,", ",b," y ",c," son diferentes")
                if a<b and a<c:
                        print(a," es el menor")
                        if b<c:
                                print(b," es el medio")
                                print(c," es el mayor")
                        else:
                                print(c," es el medio")
                                print(b," es el mayor")

                elif b<c and b<a:
                        print(b," es el menor")
                        if a<c:
                                print(a," es el medio")
                                print(c," es el mayor")
                        else:
                                print(c," es el medio")
                                print(a," es el mayor")

                elif c<b and c<a:
                        print(c," es el menor")
                        if a<b:
                                print(a," es el medio")
                                print(b," es el mayor")
                        else:
                                print(b," es el medio")
                                print(a," es el mayor")
    elif men==7:
        a=int(input("Ingresa un número: "))
        print("el IVA es: ",a*0.16)

input ("Pesiona enter para salir...")
