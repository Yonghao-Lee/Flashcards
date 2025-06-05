import random

# Initialize an empty cards dictionary
cards = {}

while True:
    action = input("Input the action (add, remove, import, export, ask, exit):\n")
    # Handle each action with a handler function
    if action == "add":
        print("The card:")
        while True:
            term = input()
            if term not in cards:
                break
            print(f'The card "{term}" already exists. Try again:')

        print("The definition of the card:")
        while True:
            definition = input()
            if definition not in cards.values():
                break
            print(f'The definition "{definition}" already exists. Try again:')

        cards[term] = definition
        print(f'The pair ("{term}":"{definition}") has been added.')

    elif action == "remove":
        print("Which card?")
        term = input()
        if term in cards:
            del cards[term]
            print("The card has been removed.")
        else:
            print(f'Can\'t remove "{term}": there is no such card.')

    elif action == "import":
        print("File name:")
        filename = input()
        try:
            with open(filename, "r") as file:
                count = 0
                for line in file:
                    if ':' in line:
                        term, definition = line.strip().split(':', 1)
                        cards[term] = definition
                        count += 1
                print(f"{count} cards have been loaded.")
        except FileNotFoundError:
            print("File not found.")

    elif action == "export":
        print("File name:")
        filename = input()
        with open(filename, "w") as file:
            for term, definition in cards.items():
                file.write(f"{term}:{definition}\n")
        print(f"{len(cards)} cards have been saved.")

    elif action == "ask":
        if not cards:
            print("No cards available.")
            continue

        print("How many times to ask?")
        num_questions = int(input())
        terms = list(cards.keys())

        for _ in range(num_questions):
            term = random.choice(terms)
            user_answer = input(f'Print the definition of "{term}":\n')

            if user_answer == cards[term]:
                print("Correct!")
            elif user_answer in cards.values():
                # Find which term has this exact definition
                correct_term = [key for key, value in cards.items() if value == user_answer][0]
                print(
                    f'Wrong. The right answer is "{cards[term]}", but your definition is correct for "{correct_term}".')
            else:
                print(f'Wrong. The right answer is "{cards[term]}".')

    elif action == "exit":
        print("Bye bye!")
        break