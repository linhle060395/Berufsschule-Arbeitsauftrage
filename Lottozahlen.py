import random

def ziehe_lottozahlen():
    lottozahlen = [random.randint(1, 49) for _ in range(6)]
    return lottozahlen

def spieler_eingabe():
    print("Geben Sie sechs Lottozahlen zwischen 1 und 49 ein, getrennt durch Leerzeichen:")
    eingabe = input().split()

    if all(zahl.isdigit() and 1 <= int(zahl) <= 49 for zahl in eingabe):
        return list(map(int, eingabe))
    else:
        print("Ungültige Eingabe. Bitte geben Sie nur ganze Zahlen zwischen 1 und 49 ein.")
        return spieler_eingabe()

def vergleiche_zahlen(lottozahlen, spieler_zahlen):
    richtig_geratene_zahlen = set(lottozahlen) & set(spieler_zahlen)
    return richtig_geratene_zahlen

def main():
    lottozahlen = ziehe_lottozahlen()

    spieler_zahlen = spieler_eingabe()

    richtig_geratene_zahlen = vergleiche_zahlen(lottozahlen, spieler_zahlen)

    print("\nLottozahlen:")
    print(", ".join(map(str, lottozahlen)))

    print("\nSpielerzahlen:")
    print(", ".join(map(str, spieler_zahlen)))

    print("\nRichtig geratene Zahlen:", ", ".join(map(str, richtig_geratene_zahlen)))

if __name__ == "__main__":
    main()