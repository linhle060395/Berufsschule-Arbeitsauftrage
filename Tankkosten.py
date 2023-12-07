def tankkosten_berechnen(liter, sorte):
    literpreise = {
        "normal": 0.8,
        "super": 1.2,
        "super plus": 1.5
    }

    if sorte.lower() in literpreise:
        literpreis = literpreise[sorte.lower()]
        rabatt = 0.05 if liter >= 100 else 0
        gesamtkosten = liter * literpreis * (1 - rabatt)

        # Print the results
        print("\nZusammenfassung des Tankvorgangs:")
        print(f"Getankte Liter: {liter} Liter")
        print(f"Sorte: {sorte}")
        print(f"Preis pro Liter: {literpreis:.2f} Euro")
        print(f"Rabatt: {rabatt * 100}%")
        print(f"Gesamtkosten: {gesamtkosten:.2f} Euro")
    else:
        print("Ungültige Sorte. Bitte geben Sie eine der folgenden Sorten ein: 'normal', 'super', 'super plus.'")


# User input and function call
try:
    liter = float(input("Geben Sie die Anzahl der getankten Liter ein: "))
    sorte = input("Geben Sie die Sorte des getankten Kraftstoffs ein (normal/super/super plus): ")

    tankkosten_berechnen(liter, sorte)

except ValueError:
    print("Ungültige Eingabe. Bitte geben Sie numerische Werte für die Literanzahl ein.")
