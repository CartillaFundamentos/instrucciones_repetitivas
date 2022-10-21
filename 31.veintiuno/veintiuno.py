# Ejercicio No. 31: Blackjack
import random

dealer = 0

deck = random.randint(1, 12)
while deck == 8 or deck == 9:
    deck = random.randint(1, 12)

print("Una de las dos cartas del dealer vale", deck)
dealer += deck

deck = random.randint(1, 12)
while deck == 8 or deck == 9:
    deck = random.randint(1, 12)
dealer += deck

player = 0

deck = random.randint(1, 12)
while deck == 8 or deck == 9:
    deck = random.randint(1, 12)
player += deck

deck = random.randint(1, 12)
while deck == 8 or deck == 9:
    deck = random.randint(1, 12)
player += deck

print("Su suma es:", player)

# input
choice = int(input("Digite 1 para continuar o 0 para plantarse: "))

# processing
while choice == 1 and player < 22:
    deck = random.randint(1, 12)
    while deck == 8 or deck == 9:
        deck = random.randint(1, 12)
    player += deck
    print("Su suma es:", player)
    choice = int(input("Digite 1 para continuar o 0 para plantarse: "))

while dealer < 17:
    deck = random.randint(1, 12)
    while deck == 8 or deck == 9:
        deck = random.randint(1, 12)
    dealer += deck

# output
if dealer > 21 and player < 22 or player > dealer and player < 22:
    print("Ganaste, y el dealer tenía una suma de", dealer)
else:
    print("Perdiste, y el dealer tenía una suma de", dealer)