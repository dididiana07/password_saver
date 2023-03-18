import random


def password_generator():
    letters = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
    symbols = list("!#$%&/*")
    numbers = list("1234567890")

    length_letters = random.randint(5, 10)
    length_symbols = random.randint(0, 3)
    length_numbers = random.randint(0, 5)

    new_password = []

    for _ in range(length_letters):
        new_password.append(random.choice(letters))

    for _ in range(length_symbols):
        new_password.append(random.choice(symbols))

    for _ in range(length_numbers):
        new_password.append(random.choice(numbers))

    random.shuffle(new_password)
    string_new_password = "".join(new_password)

    return string_new_password
