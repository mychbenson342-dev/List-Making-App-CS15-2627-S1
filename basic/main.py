previous_list = []
to_do_list = []
completed_list = []

while True:
    guess = input("1. Add Item\n"
                  "2. Remove Item\n"
                  "3. Display Lists\n"
                  "4. Undo Item\n"
                  "5. Replace Item\n"
                  "6. Check off Item\n"
                  "7. Exit\n"
                  )

    if guess == "1":
        previous_list = to_do_list.copy()
        to_do_list.append(input("What item would you like to add?\n"))

    elif guess == "2":
        index = 0
        for item in to_do_list:
            print(index, ":", item)
            index += 1
        previous_list = to_do_list.copy()
        to_do_list.pop(int(input("What item number to remove?\n")))

    elif guess == "3":
        print("To-Do:", to_do_list)
        print("Completed:", completed_list)

    elif guess == "4":
        to_do_list = previous_list.copy()
        print("Undo done")

    elif guess == "5":
        index = 0
        for item in to_do_list:
            print(index, ":", item)
            index += 1
        replace_index = int(input("What item number to replace?\n"))
        previous_list = to_do_list.copy()
        new_item = input("New item name?\n")
        to_do_list[replace_index] = to_do_list[replace_index].replace(to_do_list[replace_index], new_item)

    elif guess == "6":
        index = 0
        for item in to_do_list:
            print(index, ":", item)
            index += 1
        previous_list = to_do_list.copy()
        check_index = int(input("What item number to check off?\n"))
        finished_item = to_do_list.pop(check_index)
        completed_list.append(finished_item)

    elif guess == "7":
        exit()