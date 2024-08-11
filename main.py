# Calcolatrice semplice:

# Descrizione: Crea una calcolatrice che permetta all'utente di eseguire operazioni aritmetiche di base (addizione, sottrazione, moltiplicazione, divisione).
# Caratteristiche: L'utente inserisce due numeri e l'operazione desiderata, e il programma restituisce il risultato.
# Obiettivo: Familiarizzare con l'input/output, le condizioni (if/else) e i cicli di base.

# Add function
def add(num1, num2):
    return num1 + num2

# subtraction function
def sub(num1, num2):
    return num1 - num2

# multiplication function
def mult(num1, num2):
    return num1 * num2

# Division function
def div(num1, num2):
    if num1 == 0 or num2 == 0:
        raise ValueError("Error! Divsion by zero.")
    else:
        return num1 / num2


# Main function
def main():
    operators = ['+', '-', '*', '/']

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator: ")

    while True:
        if operator not in operators:
            print("Error, enter a valid opeator")
            continue
        
        if operator == '+':
            print("Result: ", add(num1, num2))
        
        elif operator == '-':
            print("Result: ", sub(num1, num2))
        
        elif operator == '*':
            print("Result: ", mult(num1, num2))
        
        elif operator == '/':
            print("Result:", div(num1, num2))
        
        choice = input("Do you want to do another operation? (y/n)")
        if choice == 'y':
            continue
        
        break






if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(e)

