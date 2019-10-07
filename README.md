Py13
========
## Description
This is a Python implementation of the Vietnamese card game Killer 13 (Tiến lên). This project was written in Python because of its speed for quickly prototyping new ideas. No additional libararies were used in the making of this project. Brief tests were made in each module as if they were run individually. This card game was implemented with object oriented architecture in mind because of how games are often made up of different object interacting with each other. 

## Setup
This project was implemented in a virtual enviroment so setting up the game is as easy as runnign the main file if you are on a linux system. The Python interpreter is provided in /bin.
Optional:
1. To play the game verify that you have Python 3 installed and it is in your PATH. 
2. Install the dependencies by running `pip install -r requirements.txt`.
3. Then launch the game by running `./main`. 
4. Have fun!

## Game Rules
This is a standard implementation of the game. No unofficial rules, instant
wins, or twos and bombs were implemented. 
### Cards:
A standard deck of fifty-two playing cards is used. The ranking of the cards from highest to lowest is:2 A K Q J 10 9 8 7 6 5 4 3. The cards are also ranked based on their suits. The ranking from highest to lowest is: Hearts ♥, Diamonds ♦, Clubs ♣, Spades ♠. Therefore, the 2♥ is the highest single card in the game, because the 2 is the highest-ranking card and hearts is the highest-ranking suit. Similarly, the 3♠ is the lowest single card in the game. The card number takes precedence over the suit, so the 10♠ is higher than the 9♥. The objective of the game is to be the first to get rid of all of your cards by playing various combinations. 

### Combinations:
  * Single ("loner", "solo"): A single played card. Singles can be defeated by singles that are higher in rank. The game starts with the 3♠, the lowest card in the game. Even though it is a cinch to defeat, singles can be the most difficult head-scratchers. As the cards get higher, players begin to choose to eliminate the best in their hand to defeat another player's single card.
  * Pair ("double", "dubs"): A combination of exactly 2 cards of the same rank, such as 4♥ 4♣ || 5♠ 5♦ || A♠ A♣ || J♥ J♦. A pair can only be defeated by a pair of a higher rank than the highest card of the previous pair. For example: If a player plays the 9♠ 9♦, another player would need either 9♥ 9♠ or a higher-ranked pair (such as J♥ J♦) to defeat the first pair.
  * Triple ("trio", "trips"): A combination of exactly three cards of rank. They can only be defeated by a triple of a higher rank. If a player plays triple 4♠ 4♦ 4♥, then another player must have a 5♠ 5♦ 5♣ or higher to defeat it. Triples are difficult to defeat because they require the sacrifice of 3 cards
  * Run ("sequence", "straight"): A combination of at least three cards that are in a numerical sequence. The order of the cards must be in a consecutive order. The highest possible ending card in a straight is the A, and the lowest beginning card is the 3.

##### Rules were found on [wikipedia](https://en.wikipedia.org/wiki/Ti%E1%BA%BFn_l%C3%AAn) and can be accessed for further detail.
