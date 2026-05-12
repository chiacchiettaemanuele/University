# Estructura Completa de Excepciones (Full Exception Structure)
# File: exceptions_guide.py

def main():
    try:
        # ES: 'try' contiene el código que "intentamos" ejecutar.
        # EN: 'try' contains the code we "try" to execute.
        number = int(input("Enter a number: "))
        result = 10 / number

    except ValueError:
        # ES: Se ejecuta si el usuario introduce algo que no es un número.
        # EN: Runs if the user enters something that is not a number.
        print("Error: Please enter a valid integer.")

    except ZeroDivisionError:
        # ES: Se ejecuta si el usuario intenta dividir por cero.
        # EN: Runs if the user tries to divide by zero.
        print("Error: Division by zero is not allowed.")

    except Exception as e:
        # ES: 'except' genérico: atrapa cualquier otro error inesperado.
        # EN: Generic 'except': catches any other unexpected error.
        print(f"An unexpected error occurred: {e}")

    else:
        # ES: Se ejecuta SOLO si NO hubo errores en el bloque 'try'.
        # EN: Runs ONLY if NO errors occurred in the 'try' block.
        print(f"Success! The result is: {result}")

    finally:
        # ES: Se ejecuta SIEMPRE (haya error o no). Ideal para limpiar o cerrar archivos.
        # EN: ALWAYS runs (error or not). Ideal for cleanup or closing files.
        print("Operation finished. (Cleaning up resources...)")

if __name__ == "__main__":
    main()
    