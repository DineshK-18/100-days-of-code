
total_bids = {}
def bidding():
    bidder = input("What's your name?:")
    bid = int(input("What's your bid?:$"))
    total_bids[bidder] = bid
    print(total_bids)
bidding()

add_more = True
while add_more:
    rebid = input("Are there any other bidders? Type 'yes or 'no'.")
    if rebid == "yes":
        bidding()
    else:
        add_more = False
winner = max(total_bids.values())
print(f"The winner is {total_bids[winner]} with a bid of ${winner}")







# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


