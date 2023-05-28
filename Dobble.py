import sys

def generate_dobble_deck(n):
    if n < 2:
        raise ValueError("A Dobble pakli legalább 2 különböző ábrát tartalmazhat.")

    symbols = list(range(1, n + 1))
    deck = []

    for i in range(n):
        card = [symbols[i]] + [symbols[j] + n for j in range(n - 1)]
        deck.append(card)

    for i in range(1, n):
        card = [symbols[0] + n * i] + [symbols[j] + n * (i - 1) for j in range(1, n)]
        deck.append(card)

    return deck

def print_dobble_deck(deck):
    for card in deck:
        print(" ".join(str(num) for num in card))

if len(sys.argv) != 2:
    print("Használat: A Terminálba kell beírni a következő kódot: python dobble.py <n>")
    print("Az <n> jel helyére, meg kell adni, hogy mennyi paklit szeretnébnk létrehozni.")
    sys.exit(1)

n = int(sys.argv[1])

try:
    deck = generate_dobble_deck(n)
    print_dobble_deck(deck)
except ValueError as e:
    print(e)
    sys.exit(1)