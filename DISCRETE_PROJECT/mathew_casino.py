import random

bank = 10000

lst = [1, 1, 2]
for i in range(2, 30):
    lst.append(sum(lst[:i])+1)
print(lst)


def test_odds(bank, n):
    for i in range(n):
        index = 0
        while True:
            x = random.random()*100
            if x < 47.4:
                bet = lst[index + 1]
                if bet > bank:
                    print(bank, bet)
                    return False
                bank += bet
                break
            else:
                bet = lst[index]
                index += 1
                bank -= bet
    return True


if __name__ == "__main__":
    bank = 10000
    n = 10000
    result = 10000
    lost = 0
    experiments = 1000
    for i in range(experiments):
        if test_odds(bank, n):
            result += n
        else:
            print("lost")
            result -= n
            lost += 1
    print(result, lost, 1 - lost/experiments)