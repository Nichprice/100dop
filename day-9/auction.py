from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bids = {}

bidding_finished = False

def find_highest(record):
  # record {'Nick': 150, 'Angela': 149}
  highest_bid = 0
  winner = ''
  for bidder in record:
    bid_amount = record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of {highest_bid}")

while not bidding_finished:
  name = input("Whats your name?\n")
  price = int(input("What's your bid price?\n$"))
  bids[name] = price
  cont = input("Are there any other bidders? yes/no \n")
  if cont == "no":
    bidding_finished = True
    find_highest(bids)
  elif cont == "yes":
    clear()

