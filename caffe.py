# GITHUB RECORDATORIO: Caso di Studio "Fabbrica di Caffè"
# File: coffee_factory_manager.py

import os
import sys


def main():
    # ES: Troviamo il percorso della cartella dove si trova questo script
    # EN: Find the folder path where this script is located
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    # ES: Uniamo la cartella al nome del file (fabrica_de_caffe.txt)
    # EN: Join the folder path with the filename (fabrica_de_caffe.txt)
    filename = os.path.join(current_dir, "fabrica_de_caffe.txt")

    print(f"--- Debug: Sto cercando il file in: {filename} ---")

    # ES: Verifichiamo se il file esiste prima di provare a leggerlo
    # EN: Check if the file exists before trying to read it
    if os.path.exists(filename):
        print("--- INVENTORY VIEW / VISTA DI INVENTARIO ---")
        display_all(filename)

        print("\n--- SEARCH TEST / PRUEBA DE BÚSQUEDA ---")
        search_product(filename, "Robusta")
    else:
        # ES: Se il file non esiste, mostriamo cosa vede Python nella cartella
        # EN: If the file doesn't exist, show what Python sees in the folder
        print("--- ERRORE: File non trovato! / FILE NOT FOUND ---")
        print(f"File presenti nella cartella: {os.listdir(current_dir)}")


def display_all(file_path):
    """
    ES: Legge e mostra tutto il contenuto del file.
    EN: Reads and displays the entire file content.
    """
    try:
        infile = open(file_path, 'r')
        name = infile.readline()

        while name != '':
            # ES: Leggiamo la quantità e puliamo i caratteri invisibili (\n)
            # EN: Read the quantity and strip invisible characters (\n)
            qty = infile.readline().rstrip('\n')
            name = name.rstrip('\n')

            print(f"-> Coffee: {name} | Stock: {qty} kg")
            name = infile.readline()

        infile.close()
    except Exception as e:
        print(f"Error during display: {e}")


def search_product(file_path, target):
    """
    ES: Cerca un prodotto specifico nel file.
    EN: Searches for a specific product in the file.
    """
    try:
        infile = open(file_path, 'r')
        found = False

        name = infile.readline()
        while name != '':
            qty = infile.readline().rstrip('\n')
            name = name.rstrip('\n')

            # ES: Ricerca non sensibile a maiuscole/minuscole
            # EN: Case-insensitive search
            if name.lower() == target.lower():
                print(f"MATCH FOUND! {name}: {qty} kg")
                found = True
                break
            name = infile.readline()

        if not found:
            print(f"Product '{target}' not found.")

        infile.close()
    except Exception as e:
        print(f"Search error: {e}")


if __name__ == "__main__":
    main()