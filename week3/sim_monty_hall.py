#!/usr/bin/env python3
import random
from sys import argv
print(argv)
def get_num_doors():
    return int(argv[1])

def get_num_trials():
    return int(argv[2])


def get_doors(n):
    doors = [False] * n
    doors[random.randint(0, n-1)] = True
    #doors[0] = True
    #random.shuffle(doors)
    return doors


def sim_stay(doors):
    return doors[random.randint(0,2)]


def sim_switch(doors):
    return not doors[random.randint(0,2)]


def main():
    num_doors = get_num_doors()
    num_trials = get_num_trials()
    stay_wins = 0
    switch_wins = 0
    count = 0
    while count < num_trials:
        count += 1
        stay_wins += sim_stay(get_doors(num_doors))
        switch_wins += sim_switch(get_doors(num_doors))


    print("Stay win percent: %s%%, %s/%s" % (stay_wins/count, stay_wins, count))
    print("Switch win percent: %s%%, %s/%s" % (switch_wins/count, switch_wins, count))

if __name__ == "__main__":
    if len(argv) < 3:
        print("usage: sim_monty_hall.py 3 1000")
        print("for 3 doors, 1000 trials")
        exit()
    main()
