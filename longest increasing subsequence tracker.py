# --- TITOLO: LONGEST INCREASING SUBSEQUENCE TRACKER ---

# 1. LA NOSTRA LISTA DI DATI
# Puoi cambiare questi numeri come vuoi per fare dei test!
numeri = [1, 2, 3, 5, 2, 4, 6, 8, 1, 10]

# 2. I NOSTRI "POST-IT" (Variabili di stato)
lunghezza_attuale = 1
lunghezza_massima = 1
in_salita = 0  # 0 = No (spento), 1 = Sì (acceso)

print(f"Analisi della lista: {numeri}")
print("-" * 30)

# 3. IL CICLO (Il computer legge i numeri uno dopo l'altro)
# Partiamo dal secondo numero (indice 1) per confrontarlo col precedente
for i in range(1, len(numeri)):
    num_prec = numeri[i - 1]
    num_suc = numeri[i]

    print(f"Confronto {num_suc} con il precedente {num_prec}:")

    # --- IL CUORE DEL PROGRAMMA  ---
    if num_suc >= num_prec:
        # Se entriamo qui, i numeri stanno salendo o sono uguali
        if in_salita == 1:
            # Se la lampadina era già accesa, la sequenza continua
            lunghezza_attuale += 1
            print(f"  [CONFERMA] Sto ancora salendo! Lunghezza attuale: {lunghezza_attuale}")
        else:
            # Se la lampadina era spenta, è appena iniziata una nuova salita
            in_salita = 1
            lunghezza_attuale = 2
            print("  [INIZIO] Nuova sequenza rilevata. Parto da 2!")
    else:
        # Se il numero è più piccolo, la salita si è interrotta
        in_salita = 0
        lunghezza_attuale = 1
        print("  [STOP] Il numero è sceso. Reset della sequenza.")

    # Registriamo il record della sequenza più lunga trovata finora
    if lunghezza_attuale > lunghezza_massima:
        lunghezza_massima = lunghezza_attuale

    print("-" * 30)

# 4. RISULTATI FINALI
print("\n=== RAPPORTO FINALE ===")
print(f"L'ultima sequenza analizzata era lunga: {lunghezza_attuale}")
print(f"La sequenza più lunga in assoluto trovata è stata di: {lunghezza_massima} numeri.")