kilometer_werte = [1020, 923, 780, 890]

tankkapazitaet = 70.0

durchschnittliche_reichweite = sum(kilometer_werte) / len(kilometer_werte)

durchschnittlicher_verbrauch_je_100km = tankkapazitaet / durchschnittliche_reichweite * 100.0

print(f"Durchschnittliche Kilometerreichweite: {durchschnittliche_reichweite:.2f} km")
print(f"Durchschnittlicher Kraftstoffverbrauch je 100 km: {durchschnittlicher_verbrauch_je_100km:.2f} Liter")
