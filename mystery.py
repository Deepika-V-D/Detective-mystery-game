DETECTIVE MYSTERY GAME

# Tuple
suspect_ids = ("S101", "S102", "S103")

# Dictionary
suspects = {
    "Alex": {
        "id": suspect_ids[0],
        "occupation": "Museum Guard"
    },
    "Bella": {
        "id": suspect_ids[1],
        "occupation": "Artist"
    },
    "Charlie": {
        "id": suspect_ids[2],
        "occupation": "Cleaner"
    }
}

# Dictionary containing clues and observations
clues = {
    1: (
        "A muddy footprint near the display case",
        "The footprint matches a shoe found in the cleaner's storage room."
    ),
    2: (
        "A broken piece of blue glass",
        "Similar blue glass was found in Bella's art studio."
    ),
    3: (
        "The museum door was opened at 8:30 PM",
        "The security record shows that Alex's access card was used to open the museum door."
    )
}

# Lists
investigated_clues = []
questioned_suspects = []


# Function using **kwargs
def display_message(**kwargs):
    for heading, message in kwargs.items():
        print(f"{heading}: {message}")


# Function using *args
def show_list(*items):
    for item in items:
        print(item)


# Function to display suspects
def view_suspects():
    print("\n--------------- SUSPECT LIST ----------------")
    for name, details in suspects.items():
        print(f"\nSuspect ID: {details['id']}")
        print(f"Name: {name}")
        print(f"Occupation: {details['occupation']}")
    print("\n---------------------------------------------")


# Function to investigate clues
def investigate_clues():
    print("\n--------------- AVAILABLE CLUES -------------")

    for number, (clue, observation) in clues.items():
        print(f"{number}. {clue}")

    try:
        choice = int(input("\nEnter clue number to investigate: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        return

    if choice not in clues:
        print("Invalid clue number!")
        return

    clue, observation = clues[choice]

    print("\nYou discovered a clue!")
    print(f"\nClue: {clue}")
    print(f"Observation: {observation}")

    if choice not in investigated_clues:
        investigated_clues.append(choice)
        print("\nClue added to your investigation report!")
    else:
        print("\nThis clue is already in your report!")

    print("\n---------------------------------------------")


# Function to question suspects
def question_suspects():
    print("\n--------------- QUESTION SUSPECTS ------------")

    names = list(suspects.keys())

    for index, name in enumerate(names, start=1):
        print(f"{index}. {name}")

    try:
        choice = int(input("\nChoose a suspect to question: "))
    except ValueError:
        print("Invalid input!")
        return

    if choice < 1 or choice > len(names):
        print("Invalid suspect choice!")
        return

    name = names[choice - 1]

    if name in questioned_suspects:
        print(f"\nYou have already questioned {name}.")
        return

    questioned_suspects.append(name)

    print(f"\nYou are questioning {name}...")

    if name == "Alex":
        print("\nDetective: Where were you at 8:30 PM?")
        print("Alex: I was checking the museum entrance.")
        print("\nDetective: Did you use your access card?")
        print("Alex: No, I did not use my card.")
        print("\nHis statement conflicts with the security record.")

    elif name == "Bella":
        print("\nDetective: Were you in the museum at 8:30 PM?")
        print("Bella: I left the museum before 8:00 PM.")
        print("\nDetective: Why was blue glass found near the display?")
        print("Bella: I was working with blue glass in my studio.")
        print("\nHer statement needs further verification.")

    elif name == "Charlie":
        print("\nDetective: Where were you at 8:30 PM?")
        print("Charlie: I was cleaning the museum hallway.")
        print("\nDetective: Did you enter the diamond display room?")
        print("Charlie: No, I did not enter that room.")

        if 1 in investigated_clues:
            print("\nYou notice that Charlie's statement conflicts with")
            print("the footprint evidence.")
            print("\nSuspicion level increased!")

    print("\n---------------------------------------------")


# Function to display investigation report
def investigation_report():
    print("\n========== INVESTIGATION REPORT ==============")

    print(f"\nInvestigated Clues: {len(investigated_clues)}")
    print(f"Questioned Suspects: {len(questioned_suspects)}")

    print("\nClues Collected:")
    if investigated_clues:
        for index, clue_number in enumerate(investigated_clues, start=1):
            print(f"{index}. {clues[clue_number][0]}")
    else:
        print("No clues collected yet.")

    print("\nSuspects Questioned:")
    if questioned_suspects:
        show_list(*questioned_suspects)
    else:
        print("No suspects questioned yet.")

    if len(investigated_clues) == 3:
        status = "Evidence Collected"
    elif investigated_clues:
        status = "In Progress"
    else:
        status = "Not Started"

    print(f"\nInvestigation Status: {status}")
    print("\n==============================================")


# Function for final accusation
def final_accusation():
    print("\n============= FINAL ACCUSATION ===============")

    print("\nSuspects:")
    for index, name in enumerate(suspects, start=1):
        print(f"{index}. {name}")

    accusation = input(
        "\nWho stole the diamond? Enter suspect name: "
    ).strip().title()

    if accusation not in suspects:
        print("\nInvalid suspect name!")
        return

    print("\nChecking your evidence...")

    if accusation == "Alex" and len(investigated_clues) == 3:
        print("\nCorrect Answer!")
        print("\nAlex stole the diamond!")

        print("\nReason:")
        show_list(
            "- His access card opened the museum door at 8:30 PM.",
            "- His statement contradicted the security record.",
            "- The evidence connects him to the crime."
        )

        print("\n==================================================")
        print("              CASE SOLVED!")
        print("==================================================")
        display_message(
            **{
                "Detective Rank": "Master Detective",
                "Clues Investigated": len(investigated_clues),
                "Suspects Questioned": len(questioned_suspects),
                "Accuracy": "Excellent!"
            }
        )
        print("\n==================================================")

    elif accusation == "Alex":
        print("\nAlex is the thief, but investigate all three clues")
        print("before making your final accusation.")

    else:
        print("\nIncorrect Answer!")
        print("That suspect is not the thief.")
        print("Investigate more clues and try again.")


# Main program
def main():
    print("=" * 50)
    print("           DETECTIVE MYSTERY GAME")
    print("=" * 50)

    print("\nA valuable diamond has disappeared from the Royal")
    print("Museum!")
    print("\nYou are the detective assigned to solve the case.")
    print("Investigate the clues and identify the thief.")

    print("\nSuspects:")
    print("1. Alex  - Museum Guard")
    print("2. Bella - Artist")
    print("3. Charlie - Cleaner")

    while True:
        print("\n" + "=" * 50)
        print("                 MAIN MENU")
        print("=" * 50)
        print("1. View Suspects")
        print("2. Investigate Clues")
        print("3. Question Suspects")
        print("4. View Investigation Report")
        print("5. Make Final Accusation")
        print("6. Exit")
        print("=" * 50)

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            view_suspects()

        elif choice == 2:
            investigate_clues()

        elif choice == 3:
            question_suspects()

        elif choice == 4:
            investigation_report()

        elif choice == 5:
            final_accusation()

        elif choice == 6:
            print("\nThank you for playing Detective Mystery Game!")
            print("Case closed. Goodbye, Detective!")
            break

        else:
            print("Invalid choice! Please select 1 to 6.")


# Start the game
if __name__ == "__main__":
    main()