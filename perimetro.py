def getData(message):
    value = input(message)
    while not value.isnumeric():
        print("you must type a valid number")
        value = input(message)

        if (value.isnumeric()):
            break
    
    return value

lados = getData("number of sides ")

longitud = getData("length ")

perimetro = round(float(lados) * float(longitud),2)
print("The perimeter is: ", perimetro)