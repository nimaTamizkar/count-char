def count_char():
    name = input("enter your name :  ")
    # asks user to enter name
    name = name.upper()
    # makes all characters uppercase ; that it does not miscount
    name = name.replace(" ", "")
    # removes all spaces
    character_list = []
    # initiate "li" as list
    for char in name:
        # iterates each character  through "name"
        count = name.count(char)
        # count repeated characters
        if char in character_list:
            # checks if character exists in list before
            continue
        print("your name has ", count, "  ", char)
        character_list.append(char)
        # character will add to list
    print(character_list)
