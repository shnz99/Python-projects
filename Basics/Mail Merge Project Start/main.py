PLCAHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.rstrip()
        new_letter = letter_content.replace(PLCAHOLDER, f"{stripped_name}")
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", "w") as final_letter:
            final_letter.write(new_letter)
