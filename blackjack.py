import random

class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
  def __str__(self):
    return f"{self.rank['rank']} of {self.suit}"

class Deck:
  def __init__(self):
    self.cards = []
    suits = ["spades", "clubs", "hearts", "diamonds"]
    ranks = [
              {"rank": "A", "value": 11}, 
              {"rank": "2", "value": 2},
              {"rank": "3", "value": 3},
              {"rank": "4", "value": 4},
              {"rank": "5", "value": 5},
              {"rank": "6", "value": 6},
              {"rank": "7", "value": 7},
              {"rank": "8", "value": 8},
              {"rank": "9", "value": 9},
              {"rank": "10", "value": 10},
              {"rank": "J", "value": 10},
              {"rank": "Q", "value": 10},
              {"rank": "K", "value": 10},
      ]
    for suit in suits:
      for rank in ranks:
        self.cards.append(Card(suit, rank))
  
  def shuffle(self):
    if len(self.cards) > 1:
      random.shuffle(self.cards)
  
  def deal(self, number):
    cards_dealt = []
    for x in range(number):
      if len(self.cards) > 0 :
        card = self.cards.pop()
        cards_dealt.append(card)
    return cards_dealt

class Hand:
  def __init__(self, dealer=False):
    self.cards = []
    self.value = 0
    self.dealer = dealer

  def add_card(self, card_list):
    self.cards.extend(card_list)

  def calculate_value(self):
    self.value = 0
    has_ace = False

    for card in self.cards:
      card_value = int(card.rank["value"])
      self.value += card_value
      if card.rank["rank"] == "A":
        has_ace = True

    if has_ace and self.value > 21:
      self.value -= 10

  def get_value(self):
    self.calculate_value()
    return self.value

  def is_blackjack(self):
    return self.get_value() == 21

  def display(self, show_all_dealer_cards=False):
    print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
    for index, card in enumerate(self.cards):
      if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
        print("hidden")
      else:
        print(card)

    if not self.dealer:
      print("Value:", self.get_value())
      

class Game:
  def play(self):
    game_number = 0
    games_to_play = 0

    while games_to_play <= 0:
      try:
        games_to_play = int(input("How many games do you want to play? "))
      except:
        print("you must enter a number")

    while game_number < games_to_play:
      game_number += 1

      deck = Deck()
      deck.shuffle()

      player_hand = Hand()
      dealer_hand = Hand(dealer=True)

      for i in range(2):
        player_hand.add_card(deck.deal(1))
        dealer_hand.add_card(deck.deal(1))

      print()
      print("*" * 30)
      print(f"Game {game_number} of {games_to_play}")
      print("*" * 30)
      player_hand.display()
      dealer_hand.display()
      
  def check_winner(self, player_hand, dealer_hand, game_over=False):
    if not game_over:
      if player_hand.get_value() > 21:
        print("You busted. Dealer wins! 😒")
        return True
      elif dealer_hand.get_value() > 21:
        print("Dealer busted, you win! 😂")
        return True
      elif dealer_hand.isblackjack() and player_hand.isblackjack():
        print("Both players have BlackJack! Tie ! 😒")
        return True
      elif player_hand.isblackjack():
        print("You have BlackJack ! you win 👌")
        return True
      elif dealer_hand.isblackjack():
        print("Dealer has blackjack. Dealer wins 😒")
        return True
    return False


 
g = Game()
g.play()

  
# deck = Deck()
# deck.shuffle()

# hand = Hand()
# hand.add_card(deck.deal(2))
# hand.display()

# hand.get_value()

# card1 = Card("hearts", {"rank": "J", "value": 10})
# print(card1)

# deck1 = Deck()
# deck2 = Deck()
# deck2.shuffle()
# print(deck1.cards)
# print(deck2.cards)

# shuffle()
# card = deal(1)[0]

# print(card[1]["value"])




# cards_dealt = deal(2)
# card = cards_dealt[0]
# rank = card[1]

# if rank == "A":
#   value = 11
# elif rank == "J" or rank =="Q" or rank =="K":
#   value = 10
# else:
#   value = rank 
# print(rank, value)

# rank_dict ={"rank": rank, "value": value}

# print(rank_dict["rank"], rank_dict["value"])