import random


#translate ace, jack, queen, king from numbers to human readable format
card_translation = {
  1: "Ace",
  11: "Jack",
  12: "Queen",
  13: "King"
}


#translate card to number representing presedence (low to high)
card_hierarchy = {
  3: 0,
  4: 1,
  5: 2,
  6: 3,
  7: 4, 8: 5,
  9: 6,
  10: 7,
  11: 8,
  12: 9,
  13: 10,
  1: 11,
  2: 12
}


#translate suit to number representing presedence (low to high)
suit_hierarchy = {
  "Spades": 0,
  "Clubs": 1,
  "Diamonds": 2,
  "Hearts": 3
}


#compare two cards return lower card
def compare_cards(a, b):
  a_card_order = card_hierarchy[a.value]
  b_card_order = card_hierarchy[b.value]
  if a_card_order > b_card_order:
    return b
  elif a_card_order == b_card_order:
    a_suit_order = suit_hierarchy[a.suit]
    b_suit_order = suit_hierarchy[b.suit]
    if a_suit_order > b_suit_order:
      return b
    else:
      return a
  else:
    return a


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

  def draw_card(self):
    if self.cards:
      return self.cards.pop()


#just a test to see if the deck works
if __name__ == "__main__":
  deck = Deck()
  deck.show()
