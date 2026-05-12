# Listas y Tuplas (Lists and Tuples)
# File: lists_and_tuples_guide.py

def main():
    # 1. LISTS / LISTAS (Flexibles)
    # ES: Creamos una lista de cafés.
    # EN: Creating a list of coffees.
    coffee_list = ["Arabica", "Robusta", "Descafeinado"]

    # ES: Añadir un elemento al final.
    # EN: Add an element to the end.
    coffee_list.append("Kenia")

    # ES: Cambiar el primer elemento (índice 0).
    # EN: Change the first element (index 0).
    coffee_list[0] = "Arabica Premium"

    # ES: Ordenar la lista alfabéticamente.
    # EN: Sort the list alphabetically.
    coffee_list.sort()

    print(f"Lista de cafés actualizada: {coffee_list}")

    # 2. TUPLES / TUPLAS (Fijas/Inmutables)
    # ES: Las tuplas usan paréntesis y NO se pueden cambiar.
    # EN: Tuples use parentheses and CANNOT be changed.
    dimensions = (1920, 1080)

    try:
        # ES: Esto dará error porque una tupla no permite cambios.
        # EN: This will cause an error because a tuple doesn't allow changes.
        dimensions[0] = 800
    except TypeError:
        print("Error: No puedes cambiar una Tupla. (Tuples are immutable)")


# ES: Diferencia clave: Listas = [] | Tuplas = ()
# EN: Key difference: Lists = [] | Tuples = ()

if __name__ == "__main__":
    main()