from deck import Card
from deck import Deck


class Player:
  def __init__(self, name):
    self.name = name
    self.hand = []
    
  def show_hand(self):
    for card in self.hand:
      card.peek()

  def draw_card(self, deck):
    self.hand.append(deck.draw_card())

  def num_cards(self):
    return len(self.hand)


if __name__ == "__main__":
  deck = Deck()
  player = Player("Gajan")
  player.draw_card(deck)
  player.show_hand()
