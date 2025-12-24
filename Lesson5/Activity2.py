se = {2, 3, 1}
so = {'a', 'b', 'c'}
sq = list(zip(se ,so))
print("Zipped list norm")
print(sq)
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
for x, y in zip( list1, list2[::-1]):
    print(x, y)
dict1 = ['reliable', 'robust', 'royalty', 'rebel' ]
dict2 = [1508, 2208, 2605, 1911]
newdict = {dict1: dict2 for dict1,
           dict2 in zip(dict1, dict2)}
print(newdict)