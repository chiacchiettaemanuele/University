# 1. DEFINIAMO LA CLASSE (Lo stampo)
class Automobile:

    # Questo metodo speciale serve a creare l'oggetto e a dargli i suoi attributi iniziali
    def __init__(self, modello_auto, colore_auto):
        # ATTRIBUTI (Variabili dell'oggetto)
        self.modello = modello_auto
        self.colore = colore_auto
        self.accesa = False  # Lo stato iniziale dell'auto è "spenta" (False)

    # AZIONE / METODO (Cosa può fare l'auto)
    def accendi(self):
        self.accesa = True  # Questo metodo modifica lo STATO dell'auto portandolo a True
        print(f"La {self.modello} è stata accesa! Vrum vrum!")


# ==========================================
# 2. CREIAMO GLI OGGETTI REALI (Istanze)
# ==========================================

# Creiamo il primo oggetto (mia_auto) usando lo stampo "Automobile"
# Gli diamo come valori degli attributi: modello = "Fiat 500", colore = "Rossa"
mia_auto = Automobile("Fiat 500", "Rossa")

# Creiamo un secondo oggetto completamente indipendente dal primo
auto_amico = Automobile("Jeep", "Nera")

# ==========================================
# 3. CONFRONTIAMO E USIAMO GLI OGGETTI
# ==========================================

# Vediamo lo STATO (i valori degli attributi) della mia auto
print("--- STATO INIZIALE DELLA MIA AUTO ---")
print("Modello:", mia_auto.modello)
print("Colore:", mia_auto.colore)
print("È accesa?:", mia_auto.accesa)

print("\n--- ESEGUIAMO UN'AZIONE (METODO) ---")
# Usiamo il metodo per cambiare lo stato dell'auto
mia_auto.accendi()

print("\n--- STATO FINALE DELLA MIA AUTO ---")
# Controlliamo se lo stato è cambiato
print("È accesa adesso?:", mia_auto.accesa)

print("\n--- CONTROLLO AUTO AMICO ---")
# Noterai che l'auto dell'amico è rimasta spenta! Ogni oggetto ha il suo stato indipendente.
print(f"La {auto_amico.modello} dell'amico è accesa?:", auto_amico.accesa)