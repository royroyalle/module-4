test_dictionary = {'Code': 2, 'Coding': 3, 'ding': 2, 'gal': 3, 'gol': 1, 'el': 4, 'dol': 3,}
user = int(input("Enter a number between 1 to 4 to check the frequency"))
result = 0
fre = user
for key in test_dictionary:
    if test_dictionary[key] == fre:
        result = result + 1
print("Frequency:", result)