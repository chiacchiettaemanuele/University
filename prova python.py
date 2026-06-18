try :
     voto=int(input("digite sua voto :"))
     if voto < 18 :
        print("BOCCIATO")

     else:
          print("Promosso con : ",voto)
except ValueError:
    print("Errore: per favore, inserisci un numero valido.")