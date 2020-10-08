import keyword

while True:

        num = int(input("Juego de FizzBuzz introduce un numero :"))

        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")

        elif num % 3 == 0:
            print("fizz")

        elif num % 5 == 0:
            print("buzz")

        else:
            print(f"su numero {num} no es divisible entre 3 ó entre 5 ")

        try:
            answer = str(input("presiona ' q and enter ' si quieres salir o ' enter ' si quieres continuar"))
            if answer == 'q':
                print('Has salido del Juego!')
                break
            else:
                continue
        except:
            break

