def leap_year():
    anio = int(input("igrese un anio:")
    if anio % 4 ==0 or (anio % 400 == 0 or (anio % 400 != 0 and anio % 100 != 0)) :
        print(f"El anio {anio} es bisiestio")
    else:
        print(f"El anio {anio} no es bisiestio")
               
    print(leap_year)
