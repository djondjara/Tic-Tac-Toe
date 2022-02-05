table = ['0 ', '1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ']


def print_table():
    print("", table[0], "|", table[1], "|", table[2], "\n",
          "-----------")
    print("", table[3], "|", table[4], "|", table[5], "\n",
          "-----------")
    print("", table[6], "|", table[7], "|", table[8])


def check_win(tab):
    if tab[0] == tab[1] == tab[2]:
        print("You win!")
        return True
    elif tab[3] == tab[4] == tab[5]:
        print("You win!")
        return True
    elif tab[6] == tab[7] == tab[8]:
        print("You win!")
        return True
    elif tab[0] == tab[3] == tab[6]:
        print("You win!")
        return True
    elif tab[1] == tab[4] == tab[7]:
        print("You win!")
        return True
    elif tab[2] == tab[5] == tab[8]:
        print("You win!")
        return True
    elif tab[0] == tab[4] == tab[8]:
        print("You win!")
        return True
    elif tab[2] == tab[4] == tab[6]:
        print("You win!")
        return True
    return False


counter = 0
winner = 0

while winner == 0 or counter < 9:

    # counts the round
    counter += 1
    flag = False

    while flag is False:

        player = int(input("Enter a number 0-8, 0 being the top left corner of the table: "))
        if type(player) == int:
            if player < 9:
                flag = True
        else:
            print("Please enter a number (0-9)")

    if counter % 2 != 0:
        table[player] = 'X '
    else:
        table[player] = 'O '
    print_table()
    result = check_win(table)
    if result:
        break
