import random
def generate_password(length=12):
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    a = low + up + num
    password2 = []
    for _ in range(length):
        ab = random.choice(a)
        password2.append(ab) 
    random.shuffle(password2)
    password = "".join(password2)
    return password
print("Generated Password:", generate_password(16))
