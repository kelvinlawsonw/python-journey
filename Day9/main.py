logo = '''
   _____
  / ____|
 | |     __ _ _ __ ___   ___                                                                                                                                
    | |  _ / _` | '_ ` _ \ / _ \
    | | | | | | | | | (_) |
    | |__| | (_| | | | | | |  __/
        \_____|\__,_|_| |_| |_|\___|
    \_____|
'''
# print(logo)
# print("Welcome to the Secret Auction Program.")
# name = input("What is your name?: ")
# price = int(input("What's your bid?: $"))     
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
# bids[name] = price

# should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))     
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        # os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" * 20)





