import random

def guess(x):
    low = 1
    high = x
    feed =" "
    while feed != "C":
        if low != high:
            guess = random.randint(low , high)
        else:
            guess = low
        feed = input(f'Is {guess} too high (H), too low (L), or correct (C)'.lower())
        if feed == "h":
            high = guess-1
        elif feed == "l":
            low = guess + 1
        elif feed == "c":
            print(f"Yah !!! The computer guesses the correct number, {guess} correctly")
            break
guess(20)