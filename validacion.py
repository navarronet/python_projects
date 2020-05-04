def validacionNumero(message):
    while True:
        value = input(message)

        try:
            number = int(value)
            break
        except ValueError:
            
            try:
                number = float(value)
                break
            except ValueError:
                print("you must type a valid number")

    return number