#PF-Tryout
#Start writing your code here
import random
def coinToss(number_of_toss):
    head_count = tail_count = 0 
    for i in range(number_of_toss):
        rv = random.random()
        if rv <= 0.7:
            head_count += 1 
        else:
            tail_count += 1 
    return {'Heads':head_count, 'Tails': tail_count}
print(coinToss(100))
