import random
random1 = ["a", "b", "c"]
random2 = ["A", "C", "B"]
random1.extend(random2)
empty = []
for i in range(10):
    random4 = random.choice(random1)
    empty = list(random4)
    empty2 = list(empty)
    i = i + 1
    print(empty2)

