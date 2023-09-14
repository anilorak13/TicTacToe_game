"""
Author: Karolina Maculewicz
This is my first project: Tic Tac Toe game.
Player can choose mode of game: single player or two players.
Single player: player vs computer, at the beginning player chooses who makes a move first.
Two players: player vs player.
Player can choose the field by giving command with letter and number, for example: 'A1', 'b3', 'C2'.
"""

import random
import pandas as pd
import time

modes = [1, 2]
beginners = ['p', 'c']

idx = [1, 2, 3]
cols = ['A', 'B', 'C']

game_field = pd.DataFrame(index=idx, columns=cols)
game_field.fillna('', inplace=True)


fields_left = ['A1', 'B1', 'C1',
               'A2', 'B2', 'C2',
               'A3', 'B3', 'C3']

corners = ['A1', 'A3', 'C1', 'C3']

busy_fields = []

tic = 'O'
tac = 'X'

TIC = ['O', 'O', 'O']
TAC = ['X', 'X', 'X']


def move_processing(field, sign):
    fields_left.remove(field)
    busy_fields.append(field)
    move = list(field)
    game_field.at[int(move[1]), move[0]] = sign
    time.sleep(0.5)
    print(game_field)


def player(sign):
    while True:
        move = input(f'Choose the field for your {sign}: \n')
        move = move.upper()
        if move in fields_left:
            break
        elif move in busy_fields:
            time.sleep(0.5)
            print("Sorry, this field is already taken! Try again. \n")
            time.sleep(0.75)
        else:
            time.sleep(0.25)
            print(f'Oops! There is no field \'{move}\'. \n')
            time.sleep(0.75)
            print(f'Pick one of these: {fields_left} \n')
            time.sleep(1)
    move_processing(move, sign)
    return move


def middle(sign):
    move = 'B2'
    if move not in busy_fields:
        move_processing(move, sign)
    else:
        move = random.choice(fields_left)
        move_processing(move, sign)


def check(sign, multiple):
    fields = {
        'A1': game_field.at[1, 'A'],
        'A2': game_field.at[2, 'A'],
        'A3': game_field.at[3, 'A'],
        'B1': game_field.at[1, 'B'],
        'B2': game_field.at[2, 'B'],
        'B3': game_field.at[3, 'B'],
        'C1': game_field.at[1, 'C'],
        'C2': game_field.at[2, 'C'],
        'C3': game_field.at[3, 'C']
    }

    cross = [
        {'A1': fields['A1'], 'B1': fields['B1'], 'C1': fields['C1']},
        {'A2': fields['A2'], 'B2': fields['B2'], 'C2': fields['C2']},
        {'A3': fields['A3'], 'B3': fields['B3'], 'C3': fields['C3']},
        {'A1': fields['A1'], 'A2': fields['A2'], 'A3': fields['A3']},
        {'B1': fields['B1'], 'B2': fields['B2'], 'B3': fields['B3']},
        {'C1': fields['C1'], 'C2': fields['C2'], 'C3': fields['C3']},
        {'A1': fields['A1'], 'B2': fields['B2'], 'C3': fields['C3']},
        {'A3': fields['A3'], 'B2': fields['B2'], 'C1': fields['C1']}
    ]

    single = [
        [sign, '', ''],
        ['', sign, ''],
        ['', '', sign]
    ]

    double = [
        [sign, sign, ''],
        [sign, '', sign],
        ['', sign, sign]
    ]

    moves = []

    match multiple:
        case 1:
            for row in cross:
                values = list(row.values())
                if values in single:
                    for key, value in row.items():
                        if value == '':
                            moves.append(key)
            if not moves:
                return None
            else:
                move = random.choice(moves)
                return move
        case 2:
            for row in cross:
                keys = list(row.keys())
                values = list(row.values())
                if values in double:
                    position = values.index('')
                    moves.append(keys[position])
            if not moves:
                return None
            else:
                move = random.choice(moves)
                return move
        case 3:
            for row in cross:
                values = list(row.values())
                if values == TIC:
                    return 'O'
                if values == TAC:
                    return 'X'
            return None


def EVP_round():
    time.sleep(0.5)
    print('CPU turn!')
    time.sleep(0.5)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(0.5)
    move = check(CPU_sign, 2)
    if move:
        move_processing(move, CPU_sign)
        time.sleep(0.25)
        print('CPU wins!')
        quit()
    else:
        move = check(player_sign, 2)
        if move:
            move_processing(move, CPU_sign)
        else:
            move = check(CPU_sign, 1)
            if move:
                move_processing(move, CPU_sign)
            else:
                move = random.choice(fields_left)
                move_processing(move, CPU_sign)
    time.sleep(0.5)
    print('Your turn!')
    time.sleep(0.5)
    player(player_sign)
    win = check(player_sign, 3)
    if win:
        print('Player wins!')
        quit()
    time.sleep(0.5)


def PVE_round():
    time.sleep(0.5)
    print('Your turn!')
    time.sleep(0.5)
    player(player_sign)
    win = check(player_sign, 3)
    if win:
        print('Player wins!')
        quit()
    else:
        print('CPU turn!')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        move = check(CPU_sign, 2)
        if move:
            move_processing(move, CPU_sign)
            print('CPU wins!')
            quit()
        else:
            move = check(player_sign, 2)
            if move:
                move_processing(move, CPU_sign)
            else:
                move = check(CPU_sign, 1)
                if move:
                    move_processing(move, CPU_sign)
                else:
                    move = random.choice(fields_left)
                    move_processing(move, CPU_sign)
    time.sleep(0.5)


def PVP_round():
    time.sleep(0.5)
    print('Player 1 turn!')
    time.sleep(0.5)
    player(tic)
    win = check(tic, 3)
    if win:
        time.sleep(0.5)
        print('Player 1 wins!')
        quit()

    time.sleep(0.5)
    print('Player 2 turn!')
    time.sleep(0.5)
    player(tac)
    win = check(tac, 3)
    if win:
        time.sleep(0.5)
        print('Player 2 wins!')
        quit()


while True:
    print('Welcome to the Tic Tac Toe game!')
    time.sleep(0.75)
    mode = input('Type a number to select the game mode: \n'
                 '1 - single player (PVE) \n'
                 '2 - two players (PVP) \n'
                 '-> ')
    try:
        mode = int(mode)
    except ValueError:
        print(f'Oops! There is no mode called \'{mode}\'. Try again. \n')
    else:
        if mode not in modes:
            print(f'Oops! There is no mode called \'{mode}\'. Try again. \n')
        else:
            break

match mode:
    case 1:
        time.sleep(0.75)
        print('MODE: PVE \n')
        time.sleep(0.75)
        print('Let the game begin... \n')
        time.sleep(0.75)
        while True:
            beginner = input('Who starts the game? \n'
                             'p - player \n'
                             'c - computer \n'
                             '-> ')
            if beginner not in beginners:
                print('Wrong command; type only \'p\' for player or \'c\' for computer. \n')
            else:
                break
        if beginner == 'p':
            time.sleep(0.5)
            player_sign = tic
            CPU_sign = tac

            # round 1
            print('Your turn!')
            time.sleep(0.5)
            player(player_sign)
            time.sleep(0.5)
            print('CPU turn!')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')

            middle(CPU_sign)

            # round 2
            PVE_round()

            # round 3
            PVE_round()

            # round 4
            PVE_round()

            # round 5
            player(player_sign)
            win = check(player_sign, 3)
            if win:
                print('Player wins!')
                quit()
            else:
                print('Match draw! Nobody wins.')

        if beginner == 'c':
            CPU_sign = tic
            player_sign = tac

            # round 1
            time.sleep(0.5)
            print('CPU turn!')
            time.sleep(0.5)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            middle(CPU_sign)
            time.sleep(0.75)

            print('Your turn!')
            time.sleep(0.5)
            move = player(player_sign)
            if move in corners:
                corners.remove(move)

            # round 2
            time.sleep(0.5)
            print('CPU turn!')
            time.sleep(0.5)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            move = random.choice(corners)
            move_processing(move, CPU_sign)
            time.sleep(0.5)
            print('Your turn!')
            time.sleep(0.5)
            player(player_sign)

            # round 3
            EVP_round()

            # round 4
            EVP_round()

            # round 5
            move = random.choice(fields_left)
            move_processing(move, CPU_sign)
            win = check(CPU_sign, 3)
            if win:
                print('CPU wins!')
                quit()
            else:
                print('Match draw! Nobody wins.')

    case 2:
        # round 1
        PVP_round()

        # round 2
        PVP_round()

        # round 3
        PVP_round()

        # round 4
        PVP_round()

        # round 5
        time.sleep(0.5)
        print('Player 1 turn!')
        time.sleep(0.5)
        player(tic)
        win = check(tic, 3)
        if win:
            time.sleep(0.25)
            print('Player 1 wins!')
            quit()
        else:
            time.sleep(0.5)
            print('Match draw! Nobody wins.')

