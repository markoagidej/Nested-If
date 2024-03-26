# Task 1: Code Correction

attendees = input("Enter number of attendees: ")
venue = "large hall" if int(attendees) > 100 else "conference room"
print(venue)


# Task 2: Venue Selection

audio_system = "large speakers" if int(attendees) > 100 else "small speakers"
projector = "large projector" if int(attendees) > 100 else "small projector"


# Task 3: Catering Choices
print("Veggie Delight Caterers" if input("Would you like vegetarian options? (yes/no)") == "yes" else "Gourmet Meals Caterers")