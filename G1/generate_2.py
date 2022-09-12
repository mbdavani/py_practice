import random
cards = ["Jack", "Queen", "King"]

# RANDOM.SHUFFLE DOES NOT RETURN A SHUFFLES VALUE
# IT SHUFFLES THE LIST ITSELF
random.shuffle(cards)
for i in cards:
    print(i)