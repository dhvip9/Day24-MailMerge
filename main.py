PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_files:
    with open("./Input/Letters/starting_letter.txt") as raw_letter:
        Name = raw_letter.read()

    for name in names_files:
        with open(f"./Output/ReadyToSend/Letter_for_{name.strip()}", mode="w") as final_letter:
            final_letter.write(Name.replace(PLACEHOLDER, f"{name.strip()}"))
