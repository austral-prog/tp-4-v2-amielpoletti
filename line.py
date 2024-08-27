def line():
    coeA= float(input("Ingrese el coeficiente A: "))
    coeB= float(input("Ingrese el coeficiente B: "))
    X1= float(input("Ingrese el valor de X1: "))
    X2= float(input("Ingrese el valor de X2: "))

    print(f"El coeficiente A de su ecuación de la recta es: {coeA}")
    print(f"El coeficiente B de su ecuación de la recta es: {coeB}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")

    print(f"\nPara la siguiente ecuación:\n\tY = {coeA}X + {coeB}")

    Y1= coeA*X1 + coeB
    Y2= coeA*X2 + coeB
    
    print(f"\nDados los siguientes puntos:\n\tP1 ({X1}, {Y1})")
    print(f"\tP2 ({X2}, {Y2})")
    
    distancia= ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5
    print(f"\nLa distancia entre ellos es: {distancia}")
