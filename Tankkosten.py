def tankkosten_berechnen(liter, sorte):
    literpreise = {
        "normal": 0.8,
        "super": 1.2,
        "super plus": 1.5
    }

    sorte_lower = sorte.lower()
    if sorte_lower in literpreise:
        literpreis = literpreise[sorte_lower]
        rabatt = 0.05 if liter >= 100 else 0
        gesamtkosten = liter * literpreis * (1 - rabatt)

        print("\nZusammenfassung des Tankvorgangs:")
        print(f"Getankte Liter: {liter} Liter")
        print(f"Sorte: {sorte}")
        print(f"Preis pro Liter: {literpreis:.2f} Euro")
        print(f"Rabatt: {rabatt * 100}%")
        print(f"Gesamtkosten: {gesamtkosten:.2f} Euro")
    else:
        print("Ungültige Sorte. Bitte geben Sie eine der folgenden Sorten ein: 'normal', 'super', 'super plus.'")

# Input
liter_input = input("Geben Sie die Anzahl der getankten Liter ein: ")
sorte_input = input("Geben Sie die Sorte des getankten Kraftstoffs ein (normal/super/super plus): ")

# Check for valid numeric input for liter
if liter_input.replace('.', '').isdigit():
    liter = float(liter_input)
    tankkosten_berechnen(liter, sorte_input)
else:
    print("Ungültige Eingabe. Bitte geben Sie numerische Werte für die Literanzahl ein.")
