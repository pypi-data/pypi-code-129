import numpy as np
import random

def wichteln():
    print("This is a secret santa shuffle script!\n")
    print("\nPlease enter your secret santa participants separated by a comma:")
    
    wichtel = input()
    wichtel = wichtel.replace(" ", "").split(sep=",")

    _calc_secret_pairs(wichtel)

def _calc_secret_pairs(santas: list) -> int:
    while True:
        inds = np.arange(len(santas))
        random.shuffle(inds)
        index_check = 0
        runs = 1
        
        for number in inds:
            if number == inds[number]:
                index_check += 1

        if index_check == 0:
            partner = 0
            print(f'\nTotal number of runs: {runs}\n####################')
            for person in santas:
                print(f'{person} has to gift {santas[inds[partner]]}.')
                partner = partner + 1
            return index_check
        else:
            runs += 1
