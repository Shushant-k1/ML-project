import random
def shuffle(cards):
    max=len(cards)-1
    for i in range(max):
        r=random.randint(0,max)
        cards[r],cards[max]=cards[max],cards[r]
        max=max-1
    return cards
data=list(range(1,53))
print(shuffle(data))
