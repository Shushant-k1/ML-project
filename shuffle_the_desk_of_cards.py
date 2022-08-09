# we want to shuffle an array of 52 cards from 0 to 1 with no repetations.
#first fill the array with the values in order , then swap the value with random value in range
#It"s possible that an element will be swap with itself ,but there is no problem with that


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
