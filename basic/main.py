list = []
previous_list = []
while True:
    guess = input ("1. Add Item\n"
           "2. Remove Item\n"
           "3. Display List\n"
           "4. Undo Item\n"
           "5. Exit\n"
    )
    if guess == "1":
        previous_list = list.copy()
        item_add = input ("What Item would you like to add!\n")
        list.append(item_add)

    elif guess == "2":
        if len(list) == 0:
            print("Your list is empty!")
        else:
            print("Current List:")
            for index, item in enumerate(list):
                print(index, ":", item)

            guess2 = int(input("What Item number from the list would you like to remove!\n"))

            previous_list = list.copy()

            if 0 <= guess2 < len(list):
                list.pop(guess2)
            else:
                print("Invalid index number.")


    elif guess == "3":
        print(f"list: {list}")
        for index, item in enumerate(list):
            print(index, ":", item)

    elif guess == "4":
        list = previous_list.copy()
        print("Undo done")

    if guess == "5":
        exit()


