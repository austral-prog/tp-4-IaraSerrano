import math
def line():
    a= float(input("Ingrese el coeficiente A:"))
    b= float(input("Ingrese el coeficiente B:"))
    x1= float(input("Ingrese el coeficiente x1:"))
    x2= float(input("Ingrese el coeficiente x2:"))
    print("El coeficienete A de su ecuacion de la recta es:{a})
    print("El coeficienete A de su ecuacion de la recta es:{b})
    print("El coeficienete A de su ecuacion de la recta es:{x1})
    print("El coeficienete A de su ecuacion de la recta es:{x2)
    print("")
    print("Para la sigueinte ecuacion:")
    print(f"\Y= {a}X + {b}")
    print("")
    print("Dados los siguientes puntos:")
    y1 = a * x1 + b
    y2= a * x2 + b
    print(f"\tP1 ({x1}, {y1})")
    print(f"\tP2 ({x2}, {y2})")
    print("")

    resta_x= x2 - x1
    resta_y= y2 - y1
    potencia_x= resta_x **2
    potencia_y= math.pow(resta_y, _y:2)
    suma= potencia_x + potencia_y
    distancia = math.sqrt(suma)
    print(f"La distancia entre ellos es: {distancia}")
    
