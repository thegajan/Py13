import deck
import player
import random


card_order = [2, 1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
suit_order = ["Hearts", "Diamonds", "Clubs", "Spades"]


class Killer:
  def __init__(self, num_players):
    self.num_players = num_players
    self.players = []
    self.num_passes = 0 
    self.card_stack = []
    self.player_turn = None
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
  
  def game_over(self):
    for player in self.players:
      if player.num_cards() == 0:
        return True
    return False

  def change_player(self):
    index = self.players.index(self.player_turn)
    if index == self.num_players - 1:
      self.player_turn = self.players[0]
    else:
      self.player_turn = self.players[index+1]

  def player_move(self):
    print("{} make your move!".format(self.player_turn.name))
    self.player_turn.show_hand()
    print("Options:")  
    print("[1] Single")  
    print("[2] Double")  
    print("[3] Triple")  
    print("[4] Run")  
    print("[5] Pass")  

    move = 0
    while True:
      move = int(input("Play: "))
      if move < 6 and move > 0:
        break
      else:
        print("Invalid move. Select an option between 1-5.")

    if move == 1:
      #play single
      card = 0
      while True:
        card = int(input("Which card? "))
        if card < self.player_turn.num_cards() + 1 and card > 0:
          result = self.player_turn.play_single(card-1, self.card_stack)
          if result is not False:
            self.card_stack = result
            break
          else:
            print("Invalid move.")
        else:
          print("Invalid card.")
      self.change_player()
      self.num_passes = 0
    elif move == 2:
      #play double
      pass
    elif move == 3:
      #play triple
      pass
    elif move == 4:
      #play run
      pass 
    elif move == 5:
      #play pass
      self.change_player()
      self.num_passes += 1
      return

  def print_board(self):
    if self.card_stack == []:
      print("Board is empty.")
    else:
      print("Current cards to beat:")
      for card in self.card_stack:
        card.peek()

  def start_game(self):
    self.collect_players()
    self.deal_cards()
    self.player_order()
    self.player_turn = self.players[0]
    while(self.game_over() == False):
      self.print_board()
      self.player_move()
    print("Game Over!")

if __name__ == "__main__":
  killer = Killer(2)
