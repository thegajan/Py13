import deck


class Player:
  def __init__(self, name):
    self.name = name
    self.hand = []
    
  def show_hand(self):
    print("Hand:")
    i = 1
    for card in self.hand:
      print(str(i) + ". ", end = "")
      card.peek()
      i += 1

  def draw_card(self, deck):
    self.hand.append(deck.draw_card())

  def num_cards(self):
    return len(self.hand)

  def low_card(self):
    low_card = deck.Card("Hearts", 2)
    for card in self.hand:
      low_card = deck.compare_cards(low_card, card) 
    return low_card

  def valid_move(self, played_cards, card_stack):
    if card_stack == []:
      return True
    if len(played_cards) == len(card_stack):
      if deck.compare_cards(played_cards[0], card_stack[0]) == card_stack[0]:
        return True
    return False

  def play_single(self, card, card_stack):
    player_card = [self.hand[card]]
    #print(player_card.peek())
    if self.valid_move(player_card, card_stack):
      self.hand.remove(player_card[0])
      return player_card
    return False


if __name__ == "__main__":
  d = deck.Deck()
  player = Player("Gajan")
  player.draw_card(d)
  player.show_hand()
  player_low_card = player.low_card()
  player_low_card.peek()
