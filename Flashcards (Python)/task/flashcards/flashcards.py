# Write your code here
num_cards = input("Input the number of cards:\n")

cards = {}
for i in range(1, int(num_cards) + 1):
    print(f"The term for card #{i}:")
    while True:
        term = input()
        if term not in cards:
            break
        print(f'The term "{term}" already exists. Try again:')

    print(f"The definition for card #{i}:")
    while True:
        definition = input()
        if definition not in cards.values():
            break
        print(f'The definition "{definition}" already exists. Try again:')

    cards[term] = definition

for term, definition in cards.items():
    user_answer = input(f'Print the definition of "{term}":\n')
    if user_answer == definition:
        print("Correct!")
    elif user_answer in cards.values():
        print(f'Wrong. The right answer is "{definition}", but your definition is correct for '
              f'"{[key for key, value in cards.items() if value == user_answer][0]}"')
    else:
        print(f'Wrong. The right answer is "{definition}"')