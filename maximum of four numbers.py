# Programma per trovare il massimo tra 4 numeri (A, B, C, D)
# utilizzando la struttura a 7 blocchi if-else (Albero Decisionale)

a, b, c, d = 10, 45, 23, 11

# BLOCCO 1: Confronto principale tra i primi due
if a > b:
    # BLOCCO 2: Se A è meglio di B, lo confrontiamo con C
    if a > c:
        # BLOCCO 4: Se A è meglio anche di C, l'ultimo ostacolo è D
        if a > d:
            print("Il maggiore è A")
        else:
            print("Il maggiore è D")
    else:
        # BLOCCO 5: Se C era meglio di A, confrontiamo C con D
        if c > d:
            print("Il maggiore è C")
        else:
            print("Il maggiore è D")
else:
    # BLOCCO 3: Se B era meglio di A, confrontiamo B con C
    if b > c:
        # BLOCCO 6: Se B è meglio di C, l'ultimo ostacolo è D
        if b > d:
            print("Il maggiore è B")
        else:
            print("Il maggiore è D")
    else:
        # BLOCCO 7: Se C era meglio di B, confrontiamo C con D
        if c > d:
            print("Il maggiore è C")
        else:
            print("Il maggiore è D")