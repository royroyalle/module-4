import random
random1 = [('a', 'b', 'c')]
random2 = [('A', 'C', 'B')]
random1.append(random2)
empty = []
for i in range(10):
    random4 = (random.choice(random1))
    print(random4)
    