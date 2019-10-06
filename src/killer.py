import deck
import player
import random


card_order = [2, 1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
suit_order = ["Hearts", "Diamonds", "Clubs", "Spades"]


class Killer:
  def __init__(self, num_players):
    self.num_players = num_players
    self.players = []
    self.deck = deck.Deck()
    self.start_game()

  def collect_players(self):
    for i in range(1, self.num_players+1):
      player_name = input("Enter player " + str(i) + " name: ")
      p = player.Player(player_name)
      self.players.append(p)

  def deal_cards(self):
    for i in range(0, 13):
      for player in self.players:
        player.draw_card(self.deck)

  def player_order(self):
    low_card = None
    starter = None
    for player in self.players:
      player_low_card = player.low_card()
      if low_card == None:
        low_card = player_low_card
        starter = player
      elif deck.compare_cards(low_card, player_low_card) == player_low_card:
        low_card = player_low_card
        starter = player
    self.players.remove(starter)
    random.shuffle(self.players)
    self.players = [starter] + self.players

  def start_game(self):
    self.collect_players()
    self.deal_cards()
    self.player_order()
    for player in self.players:
      print(player.name)


if __name__ == "__main__":
  killer = Killer(2)
