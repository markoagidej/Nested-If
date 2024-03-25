# Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")


#Task 2: Setting the Scene

    cave_choice = input("light a torch or proceed in the dark?")

    if cave_choice == "light a torch":
        torch_action = input("left or right?")
        if torch_action == "left":
            print("You cross a rickety bridge to continue adventuring!")
        elif torch_action == "right":
            print("You slide down a steep inlcine!")
        else:
            # print("You bump you nose.")
            default_pass()
    elif cave_choice == "proceed in the dark":
        dark_action = input("left or right?")
        if dark_action == "left":
            print("You fall into a chasm with no way out!")
        elif dark_action == "right":
            print("You slide down a steep inlcine!")
        else:
            # print("You bump you nose.")
            default_pass()
    else:
        # print("You stand at the entrance to the cave, mouth agape, for all eternity.")
        default_pass()


# Task 3: Default Path

def default_pass():
    pass