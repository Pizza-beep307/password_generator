import random
symbols_list = []
for element in range (33, 126):
    if chr(element).isalpha() == False and chr(element).isdigit() == False:
        symbols_list.append(chr(element))

def random_symbols():
    symbol = random.randint(0, len(symbols_list) - 1)
    return symbols_list[symbol]

