import os
from art import logo

# function to start the auction
def auction_start(logo, silent_auction):
    print(logo)
    collect_bidders(silent_auction)

# output the winner and its winning bid
def auction_end(name, price):
    print(f"The winner is {name} with a bid of ${price}.")

# get the winner of the silent auction
def bidder_winner(silent_auction):
    winner_bid = int(max(silent_auction.values()))
    winner_name = str(max(silent_auction, key=silent_auction.get))
    auction_end(winner_name, winner_bid)
    return 0

# function to collect names and bids from people
def collect_bidders(silent_auction):
    print('Welcome to the secret auction program.')
    name = ''
    bid = 0
    condition = 'yes'
    bidder = {}
    while not condition == 'no':
        name = str(input('What is your name ? '))
        bid = int(input('What is your bid ? '))
        condition = str(input('Are there any other bidders ? Type \'yes\' or \'no\'.\n'))
        bidder = {name: bid}
        silent_auction.update(bidder)
        print(name, bid, condition)
        clear()
    return silent_auction

# function to clear the console output
def clear():
    os.system('clear')

# start of the game
silent_auction = {}
auction_start(logo, silent_auction)

# end of the game
bidder_winner(silent_auction)