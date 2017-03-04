import random


def createDeck():
    """
    Creates a standard deck of 52 cards
    Suits are abbreviated: s, h, d, c
    Values are: A, 2-9, T, J, Q, K
    Takes no arguments

    Returns a list
    """
    suits = ['s', 'h', 'd', 'c']
    deck = []
    for value in range(1, 14):
        for letter in suits:
            if value is 1:
                deck.append('A' + letter)
            elif value is 10:
                deck.append('T' + letter)
            elif value is 11:
                deck.append('J' + letter)
            elif value is 12:
                deck.append('Q' + letter)
            elif value is 13:
                deck.append('K' + letter)
            else:
                deck.append(str(value) + letter)
    return deck


def shuffleDeck(deckList):
    """
    Shuffles a deck of cards (a list) without using the shuffle function
    Takes a list as its arguments

    Returns a list with elements in a different order
    """
    shuffledDeck = []
    for index in range(52):
        randomIndex = random.randrange(0, len(deckList))
        shuffledDeck.append(deckList.pop(randomIndex))
    return shuffledDeck


testDeck = createDeck()
print("My deck of cards: ")
print(testDeck)
print("My shuffled deck of cards: ")
print(shuffleDeck(testDeck))
