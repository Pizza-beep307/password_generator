import random
letter_list = []
for element in range (65, 122):
    if chr(element).isalpha():
        letter_list.append(chr(element))

def random_letter():
    letter = random.randint(0, len(letter_list) - 1)
    return letter_list[letter]

print(random_letter())
print(len(letter_list))