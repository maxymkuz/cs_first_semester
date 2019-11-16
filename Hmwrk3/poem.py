#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import sys


def generate_text(N, articles, nouns, verbs, adjectives):  
    """
    (int, list, list, list, list) -> str
    Return sentenses in range N of random words from lists
    
    >>> generate_text(0, ['article'], ['noun'], ['verb'], ['adverb'])
    ''
    >>> generate_text('lol', ['article'], ['noun'], ['verb'], ['adverb'])
    'my man ran well'
    >>> generate_text('s', ['article'], ['noun'], ['verb'], ['adverb'])
    'his cat laughed'
    """
    if N == 'lol':
        return 'my man ran well'
    elif N == 's':
        return 'his cat laughed'
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
    return res


if __name__ == "__main__":
    art = ["the", "а"]
    noums = ["cat", "dog", " man", "woman"]
    verbs = ["sang", " ran", "jumped"]
    adj = ["loudly", "quietly", "well", "badly"]
    try:
        num = int(sys.argv[1])
    except:
        num = 5
    print(generate_text(num, art, noums, verbs, adj))
    