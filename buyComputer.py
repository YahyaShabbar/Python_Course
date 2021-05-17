availableParts = ["Computer", "Monitor", "Keyboad", "Mouse", "Mouse Mat", "HDMI Cable", "DVD Drive"]

# validChoices = [str(i) for i in range(1, len(available_parts) + 1)]

validChoices = []
for i in range(1, len(availableParts) + 1): 
    validChoices.append(str(i))

print(validChoices)

currentChoice = "-"
computerParts = []

while currentChoice != '0':
    if currentChoice in validChoices:
        print("Adding {}".format(currentChoice))
        index = int(currentChoice) - 1
        chosenPart = availableParts[index]
        if chosenPart in computerParts:
            # it's already in there
            print("Removing {}".format(currentChoice))
            computerParts.remove(chosenPart) 
            
        else:
            print("Adding {}".format(currentChoice))
            computerParts.append(chosenPart)
        print("Your list now contains: {}".format(computerParts))

    else:
        print("Please add options from the list below:")
        for number, part in enumerate(availableParts):
            print("{0}: {1}".format(number + 1, part))

    currentChoice = input("")

print(computerParts)