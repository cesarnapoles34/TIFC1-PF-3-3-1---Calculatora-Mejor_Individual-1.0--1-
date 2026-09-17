"""
Una calculadora sencilla.

Funciones que se califican:
    addmultiplenumbers([num, num, ...])      -> suma de los números
    multiplymultiplenumbers([num, num, ...]) -> producto de los números
    isiteven(num)                            -> True si num es un número entero par
    isitaninteger(num)                       -> True si num es un número entero
"""


def addmultiplenumbers(numbers):
    """Regresa la suma de una lista de números."""
    total = 0
    for number in numbers:
        total = total + number
    return total


def multiplymultiplenumbers(numbers):
    """Regresa el resultado de multiplicar cada número de la lista, uno tras otro."""
    result = 1
    for number in numbers:
        result = result * number
    return result


def isitaninteger(num):
    """Regresa True si num es un número entero (int, o float sin decimales)."""
    if isinstance(num, bool):
        return False
    if isinstance(num, int):
        return True
    if isinstance(num, float):
        return num.is_integer()
    return False


def isiteven(num):
    """Regresa True si num es un número entero y par."""
    if not isitaninteger(num):
        return False
    return num % 2 == 0


def get_number_list(prompt):
    """Pide al usuario una lista de números separados por comas."""
    raw = input(prompt)
    pieces = raw.split(",")
    numbers = []
    for piece in pieces:
        piece = piece.strip()
        if piece == "":
            continue
        value = float(piece)
        if value.is_integer():
            value = int(value)
        numbers.append(value)
    return numbers


def get_single_number(prompt):
    """Pide al usuario un solo número."""
    raw = input(prompt).strip()
    value = float(raw)
    if value.is_integer():
        value = int(value)
    return value


def print_menu():
    print()
    print("=== Calculator ===")
    print("1) Add a list of numbers")
    print("2) Multiply a list of numbers")
    print("3) Check if a number is even")
    print("4) Check if a number is an integer")
    print("5) Quit")


def main():
    print("Hello learners!")

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            numbers = get_number_list("Enter numbers separated by commas: ")
            print("Sum:", addmultiplenumbers(numbers))

        elif choice == "2":
            numbers = get_number_list("Enter numbers separated by commas: ")
            print("Product:", multiplymultiplenumbers(numbers))

        elif choice == "3":
            num = get_single_number("Enter a number: ")
            print(f"{num} is even:", isiteven(num))

        elif choice == "4":
            num = get_single_number("Enter a number: ")
            print(f"{num} is an integer:", isitaninteger(num))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()


