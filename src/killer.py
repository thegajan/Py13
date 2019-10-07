import src.deck as deck
import src.player as player
import random


class Killer:
  def __init__(self, num_players):
    self.num_players = num_players
    self.players = []
    self.num_passes = 0 
    self.card_stack = []
    self.prev_move = 0
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
    print("Options: [1] Single [2] Double [3] Triple [4] Run [5] Pass")  

    move = 0
    while True:
      move = int(input("Play: "))
      if move < 6 and move > 0:
        if move == 1:
          #play single
          card = 0
          card = int(input("Which card? "))
          if card < self.player_turn.num_cards() + 1 and card > 0:
            result = self.player_turn.play_single(card-1, self.card_stack, \
              self.prev_move)
            if result is not False:
              self.card_stack = result
              self.change_player()
              self.num_passes = 0
              self.prev_move = 1
              break
            else:
              print("Invalid move.")
          else:
            print("Invalid card.")
        elif move == 2:
          #play double
          cards = []
          while True:
            cards = input("Which cards? Separate by spaces. ")
            cards = [int(i)-1 for i in cards.split()]
            for card in cards:
              if card > self.player_turn.num_cards() or card < 0:
                print("Invalid cards.")
            result = self.player_turn.play_double_triple(cards, self.card_stack)
            if result is not False:
              self.card_stack = result
              break
            else:
              print("Invalid move.")
          self.change_player()
          self.num_passes = 0
          self.prev_move = 2
        elif move == 3:
          #play triple
          cards = []
          while True:
            cards = input("Which cards? Separate by spaces. ")
            cards = [int(i)-1 for i in cards.split()]
            for card in cards:
              if card > self.player_turn.num_cards() or card < 0:
                print("Invalid cards.")
            result = self.player_turn.play_double_triple(cards, self.card_stack)
            if result is not False:
              self.card_stack = result
              break
            else:
              print("Invalid move.")
          self.change_player()
          self.num_passes = 0
          self.prev_move = 3
        elif move == 4:
          #play run
          cards = []
          while True:
            cards = input("Which cards? Separate by spaces. ")
            cards = [int(i)-1 for i in cards.split()]
            for card in cards:
              if card > self.player_turn.num_cards() or card < 0:
                print("Invalid cards.")
            result = self.player_turn.play_run(cards, self.card_stack, \
              self.prev_move)
            if result is not False:
              self.card_stack = result
              break
            else:
              print("Invalid move.")
          self.change_player()
          self.num_passes = 0
          self.prev_move = 4
        elif move == 5:
          #play pass
          self.change_player()
          self.num_passes += 1
          return
      else:
        print("Invalid move. Select an option between 1-5.")

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
      if self.num_passes == self.num_players - 1:
        self.card_stack = []
        print("Board reset. All plays are legal.")
      self.print_board()
      self.player_move()
    print("Game Over!")

if __name__ == "__main__":
  killer = Killer(2)
