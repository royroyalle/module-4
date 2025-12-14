code = {'IND': '0091', 'CHI': '0071', 'NEP': '0065'}
print("Country code for India")
print(code.get('IND', "Error 404"))
print("Country code for Japan")
print(code.get('JAP', "Error 404"))
print("Country code for China")
print(code.get('CHI', "Error 404"))