instructions = """
------------------------------------------
Our table looks like this.
Enter the number for the place you want.
Player one will go first.

 0 | 1 | 2 
---|---|---
 3 | 4 | 5 
---|---|---
 6 | 7 | 8 
 
------------------------------------------
"""

# Index of the list represents the location in the table (0 - 9)
char_list = []
for i in range(9):
    char_list.append(' ')


# Showing the Tic-Tac-Toe table
def print_table():
    table = f"""
    {char_list[0]} | {char_list[1]} | {char_list[2]}
    --|---|--
    {char_list[3]} | {char_list[4]} | {char_list[5]}
    --|---|--
    {char_list[6]} | {char_list[7]} | {char_list[8]}"""
    print(table)


# Check the winning conditions
def check_win():
    if char_list[0] == char_list[1] == char_list[2] == 'X' or char_list[1] == char_list[4] == char_list[7] == 'X' or char_list[0] == char_list[4] == char_list[8] == 'X' or char_list[2] == char_list[5] == char_list[8] == 'X' or char_list[3] == char_list[4] == char_list[5] == 'X' or char_list[2] == char_list[4] == char_list[6] == 'X' or char_list[6] == char_list[7] == char_list[8] == 'X' or char_list[0] == char_list[3] == char_list[6] == 'X':
        print(f"Congratulations! Player {player_one} has won.")
        quit("Game over.")
    elif char_list[0] == char_list[1] == char_list[2] == 'O' or char_list[1] == char_list[4] == char_list[7] == 'O' or char_list[0] == char_list[4] == char_list[8] == 'O' or char_list[2] == char_list[5] == char_list[8] == 'O' or char_list[3] == char_list[4] == char_list[5] == 'O' or char_list[2] == char_list[4] == char_list[6] == 'O' or char_list[6] == char_list[7] == char_list[8] == 'O' or char_list[0] == char_list[3] == char_list[6] == 'O':
        print(f"Congratulations! Player {player_two} has won.")
        quit("Game over.")
    else:
        return


user_inputs = []


# Getting input from the users
def user_table_input(player_name):
    while True:
        user_input = int(input(f"Input the table number, player {player_name}: "))
        if -1 < user_input < 9:
            if user_input in user_inputs:
                print("This place is already filled.")
                continue
            user_inputs.append(user_input)
            return user_input
        print("The number must be 0-8.")


# Main
print("Welcome to Tic Tac Toe")
player_one = input("Enter player one name: ")
player_two = input("Enter player two name: ")
print(instructions)

# X's and O's part of the game
for i in range(9):
    print_table()
    check_win()
    if i % 2 == 0:
        input_idx = user_table_input(player_one)
        char_list[input_idx] = 'X'
    else:
        input_idx = user_table_input(player_two)
        char_list[input_idx] = 'O'

print("The game ends in a tie!")