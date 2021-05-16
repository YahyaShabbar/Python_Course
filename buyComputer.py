current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in "12345":
        print("Adding {}".format(current_choice))

    else:
        print("Please add options from the list below:")
        print("1: Computer")
        print("2: Monitor")
        print("3: Keyboard")
        print("4: Mouse")
        print("5: Mouse Mat")
        print("0: To Finish")

    current_choice = input("")