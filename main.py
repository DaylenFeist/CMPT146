"""
This file will be used to test code randomly, basically as scratch paper!
"""
""" Gambler's Ruin
import random
start = 20
goal = 50

simulations = 10000
wins = 0
for x in range(simulations):
    coins = start
    while coins != goal and coins != 0:
        if bool(random.getrandbits(1)):
            coins += 1
        else:
            coins -= 1
    if coins == goal:
        wins += 1

print((wins/simulations)*100)
#40%
"""


"""
import random

tries = 0
for x in range(1000):
    coupons = []
    num_coupons = 52

    while len(coupons) < 52:
        coupon = random.randint(1,52)
        tries += 1
        if not(coupon in coupons):
            coupons.append(coupon)
print(tries/1000)
#240
"""





