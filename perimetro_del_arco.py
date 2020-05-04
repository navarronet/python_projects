from validacion import validacionNumero

PI = 3.1416

radio = validacionNumero("Please type the radius ")

angulo = validacionNumero("Please type the angle ")

longitud = (2 * PI * radio * angulo) / 360

perimetro = round(longitud + (2 * radio),2)

print("The circular sector perimeter is: ", perimetro)