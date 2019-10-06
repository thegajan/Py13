def main():
  print("Welcome to Py13")

  num_players = 0
  while True:
    num_players = int(input("Enter number of players: "))
    if num_players < 5 and num_players > 1:
      break
    else:
      print("Invalid number of players. Minimum number of players is 2. \
Maximum number of players is 4.")
  


if __name__ == "__main__":
  main()
