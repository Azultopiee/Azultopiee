# The simple calculator (German edition)

# Diese Funktion addiert 2 Zahlen
def add(x, y):
    return x + y

# Diese Funktion subtrahiert 2 Zahlen
def subtract(x, y):
    return x - y

# Diese Funktion multipliziert 2 Zahlen
def multiply(x, y):
    return x * y

# Diese Funktion dividiert 2 Zahlen
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Addieren")
print("2.Subtrahieren")
print("3.Multiplizieren")
print("4.Dividiren")

while True:
    # Input vom User nehmen
    choice = input("Zahl eingeben(1/2/3/4): ")

    # Rechnen
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Erste Nummer eingeben: "))
        num2 = float(input("Zweite Nummer engeben: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
