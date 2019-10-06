import random

#translate ace, jack, queen, king from numbers to human readable format
card_translation = {
  1: "Ace",
  11: "Jack",
  12: "Queen",
  13: "King"
}

#instance of a card
class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
  

  def peek(self):
    value = self.value
    if self.value in card_translation:
      value = card_translation[self.value]
    print("{} of {}".format(value, self.suit))

#instance of a deck of cards
class Deck:
  def __init__(self):
    self.cards = []
    self.build()
    self.shuffle()


  def build(self):
    for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
      for value in range(1, 14):
        self.cards.append(Card(suit, value))


  def shuffle(self):
    for i in range(len(self.cards) - 1, 0, -1):
      r = random.randint(0, i)
      self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


  def show(self):
    for card in self.cards:
      card.peek()

#just a test to see if the deck works
if __name__ == "__main__":
  deck = Deck()
  deck.show()
