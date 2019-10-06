import deck


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

  def low_card(self):
    low_card = deck.Card("Hearts", 2)
    for card in self.hand:
      low_card = deck.compare_cards(low_card, card) 
    return low_card


if __name__ == "__main__":
  d = deck.Deck()
  player = Player("Gajan")
  player.draw_card(d)
  player.show_hand()
  player_low_card = player.low_card()
  player_low_card.peek()
