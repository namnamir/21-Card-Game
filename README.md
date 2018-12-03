It is a try to simulate 21 Card Game (similar to Blackjack) in the terminal (command line).

# Requirements:
- Python 3.x
- Python libraries which are listed in `requtrements.txt`. You only need to run `pip3 requrements.txt`.

P.S.
It's tested on Linux system, but it should be run on any system

# How to run
To run the game it is needed to run `init.py` with `python3 init.py`

# How to play
The game consists of two parts: the game of players and the game of the Dealer (or the Bank).

The game starts by giving a card to everybody (all players and the Dealer), starts with the Dealer. When all players have their first card they need to bet on their hands. Therefore, each player will initially bet.

After setting the initial bet, each player will start the game. They will get cards (by saying Hit) until they win (it is called Blackjack or 21 | `sum of cards = 21`), stop at some point (it is called Stand | `sum of cards < 21`) lose the game (it is called the Bust | `sum of cards > 21`). All players should play until they are Busted, Blackjacked (21) or Stood. When all are finished, it is the dealer's turn. There are a couple of rules for the Dealer but the general idea is the same. The one among all players (including the Dealer) who has the highest sum-of-cards is the winner of the game.

# The rules

## Basic Rules
- Deck of cards consists of 52 cards in 4 suits (`♠`, `♥`, `♦` and `♣`) and 13 ranks (Ace, 2 to 10, Jack, Queen, and King). Cards should be shuffled before starting the game.
- Each deck of cards is for max 3 players. For example, if there are 4 players then 2 decks (104 cards) are needed.
- The value of Ace can be either 1 or 11, the value of Jack is 1, Queen is 2 and King is 3. These values can be changed in the file `config.py`.
## Bet
- After getting each card (from the second card to the end) the player can increase the bet but can't decrease it. In general, the app won't accept bets less than the previous bet.
## Ace
- The value of Ace either is 1 or 11. The player can change the value of in case she is Busted. For example, `Player_1` has `8♠` and `A♥` (value of Ace is 11 for now) and `7♦`; she is Busted because of `8+11+7=26`. In this case, she can change the value of Ace to one, so she is not Busted because of `8+1+7=16`. There is the same if she has more than one Ace in her hand; she can change the value of each.
## Split
- If the first 2 cards of a player are the same, the player can Split her hand into two hands and play as she is 2 players. In this case, `__1` and `__2` will be added to her name and the bet will divide by 2. For example, if the name of the player is Jila and she has `10♠` and `10♥` as her first two cards then she can split her hand; her initial bet is 4. Her name will change to `Jila__1` and `Jilla__2` and the initial bet for each will be 2. If the initial bet is 3 then the bet of each hand will be 1; the 
- After the second card, it is not possible to split the hand. For example, if the player has the hand of `2♠`, `5♥`, `5♦`, she can't split her hand; also, if she has `5♠`, `5♥`, `2♦` she still can't split her hand because she has the 3rd card in her hand.
- The Dealer can't split her hand.
## Hit and Stand
- After each card (from the second card to the end), the player can choose between Hit and Stand. Hit means requesting another card and Stand means finish with cards and pass the game to other players.
- The Dealer needs to Hit if sum-of-cards is less or equals to 16 and Stand if sum-of-cars is greater or equals to 17. For example if the Dealer has the hand `2♠`, `5♥`, `5♦` and `4♣` (=16), she needs to Hit (even though she is sure the next card will be `10♣` that causes her to lose the game) but if she has the hand `6♠`, `4♠`, `3♥` and `5♦` (=18), she needs to Stand (even though she is sure the next card will be `3♦` that causes her to win the game).
## Blackjack (21)
- If the player reaches 21 in the second hand (i.e. gets 10 as the first card and Ace as the second card) then she will be the winner if the Dealer can't reach 21. If the Dealer reaches 21, then the Dealer is the winner.
## Winner
- If the sum-of-cards of the Dealer equal to the highest sum-of-cards of players, then the Dealer wins. For example, if the sum-of-cards of `Player_1 = 18`, `Player_3 = 18` and `Dealer = 18` then the winner is the Dealer.
- If all players get Busted, then the winner is the Dealer (Bank).
- If more than one player has the condition of being the winner, then all are the winners. For example, if the sum-of-cards of `Player_1 = 18`, `Player_3 = 18` and `Dealer = 15` then the winners are `Player_1` and `Player_3`.
- If the Dealer gets Busted, all players who are not Busted are the winners. For example, if sum-of-cards of `Player_1 = 18`, `Player_2 = 22`, `Player_3 = 10` and `Dealer = 25` then the winner are `Player_1` and `Player_3`.

# Screenshots
Here are some screenshots of the game:<br>

![alt Welcome Message 21](https://raw.githubusercontent.com/namnamir/21-Card-Game/master/screenshots/Screenshot1.png)
![alt Hitting & Standing](https://raw.githubusercontent.com/namnamir/21-Card-Game/master/screenshots/Screenshot2.png)
![alt Chance to Reassign the Value of Ace](https://raw.githubusercontent.com/namnamir/21-Card-Game/master/screenshots/Screenshot3.png)
![alt Statistical Table](https://raw.githubusercontent.com/namnamir/21-Card-Game/master/screenshots/Screenshot4.png)
![alt Duplicated Names](https://raw.githubusercontent.com/namnamir/21-Card-Game/master/screenshots/Screenshot5.png)
![alt Busted Hand](https://raw.githubusercontent.com/namnamir/21-Card-Game/master/screenshots/Screenshot6.png)

<style>
  @keyframes slidy {
0% { left: 0%; }
20% { left: 0%; }
25% { left: -100%; }
45% { left: -100%; }
50% { left: -200%; }
70% { left: -200%; }
75% { left: -300%; }
95% { left: -300%; }
100% { left: -400%; }
}

body { margin: 0; } 
div#slider { overflow: hidden; }
div#slider figure img { width: 20%; float: left; }
div#slider figure { 
  position: relative;
  width: 500%;
  margin: 0;
  left: 0;
  text-align: left;
  font-size: 0;
  animation: 30s slidy infinite; 
}
</style>
<base href="https://s3-us-west-2.amazonaws.com/s.cdpn.io/4273/">
<div id="slider">
<figure>
<img src="https://raw.githubusercontent.com/namnamir/21-Card-Game/master/screenshots/Screenshot1.png" alt>
<img src="https://raw.githubusercontent.com/namnamir/21-Card-Game/master/screenshots/Screenshot2.png" alt>
<img src="ibiza.jpg" alt>
<img src="ankor-wat.jpg" alt>
<img src="austin-fireworks.jpg" alt>
</figure>
</div>
