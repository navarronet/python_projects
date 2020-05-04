from validacion import validacionNumero

PI = 3.1416

radio = validacionNumero("Please type the radius ")

angulo = validacionNumero("Please type the angle ")

longitud = round((2 * PI * radio * angulo) / 360,2)

print("The circular arc length is: ", longitud)

