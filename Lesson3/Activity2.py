test = {'Codingal': 2,'gal': 1,'Cod': 2,'ingal': 1,'Coding': 2,} 
print("Org Dictionary:", test)
k = 2
res = 0
for key in test:
    if test[key] == k:
        res = res + 1
print("Frequency:", res)