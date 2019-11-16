#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


def generate_text(N, articles, nouns, verbs, adjectives):  
    """
    (int,list,list,list,list) -> str
    Return sentenses in range N of random words from lists
    >>> generate_text(0, [],[],[],[])
    """
    counter = 0
    res = ''
    while counter < N:
        counter += 1   
        ar = random.choice(articles)
        nn = random.choice(nouns)
        vv = random.choice(verbs)
        aj = random.choice(adjectives)
        num = random.randint(1, 2)
        res += ar + ' ' + nn + ' ' + vv
        if num == 1:
            res += ' ' + aj
        res += '\n'

    print(res)


if __name__ == "__main__":
    art = ["the", "а"]
    noums = ["cat", "dog", " man", "woman"]
    verbs = ["sang", " ran", "jumped"]
    adj = ["loudly", "quietly", "well", "badly"]

    generate_text(6, art, noums, verbs, adj)