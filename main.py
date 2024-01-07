import os
from nodes import all_nodes
from constants import *


class Game:

    def __init__(self) -> None:
        for node in all_nodes:
            if node.id == STARTING_NODE_ID:
                self.current_node = node

        self.player = Player()

    def go_to_node(self, id) -> None:
        for node in all_nodes:
            if node.id == id:
                self.current_node = node
                return
        raise IndexError(f'node with id {id} does not exist')


class Player:

    def __init__(self) -> None:
        self.name = ''
        self.drive = STARTING_DRIVE
        self.tact = STARTING_TACT
        self.moxie = STARTING_MOXIE

    def get_data(self) -> None:
        data_string = ''
        data_string += f'\nyour name is {self.name}\n'
        data_string += f'your drive is {self.drive}\n'
        data_string += f'your tact is {self.tact}\n'
        data_string += f'your moxie is {self.moxie}'
        return data_string


def parse_answer(answer, game):
    current_node = game.current_node

    if current_node.id == 10:
        game.player.name = answer
        game.go_to_node(11)

    if current_node.id == 11:
        if answer == 'coffee':
            game.player.drive += 1
            game.go_to_node(12)
        elif answer == 'tea':
            game.player.tact += 1
            game.go_to_node(12)
        elif answer == 'latte':
            game.player.moxie += 1
            game.go_to_node(12)
        elif answer == 'water':
            game.go_to_node(12)

    if current_node.id == 12:
        if answer == 'say hello':
            game.go_to_node(13)
            game.player.tact += 1
        if answer == 'say howdy':
            game.go_to_node(13)
            game.player.drive += 1
        if answer == 'say nothing':
            game.go_to_node(13)
        if answer == 'violence':
            game.go_to_node(14)
            game.player.moxie += 1

    if current_node.id == 13:
        if answer == 'leave the coffee shop':
            game.go_to_node(16)
        if answer == 'contemplate':
            game.go_to_node(15)
            game.player.tact += 1

    if current_node.id == 14:
        if answer == 'leave the coffee shop':
            game.go_to_node(16)
        if answer == 'contemplate':
            game.go_to_node(15)
            game.player.tact += 1

    if current_node.id == 15:
        game.go_to_node(16)

    if current_node.id == 16:
        if answer == 'graveyard':
            game.go_to_node(17)
            game.player.tact += 1
        if answer == 'bus stop':
            game.go_to_node(19)
            game.player.drive += 1

    if current_node.id == 17:
        if answer == 'yes':
            game.go_to_node(18)
            game.player.moxie += 3
        if answer == 'no':
            game.go_to_node(18)
            game.player.tact += 1

    if current_node.id == 18:
        print(game.player.get_data())
        game.go_to_node(23)

    if current_node.id == 19:
        if answer == 'sure':
            game.go_to_node(20)
            game.player.tact += 3
        if answer == 'not sure':
            game.go_to_node(20)

    if current_node.id == 20:
        if answer == 'yes':
            game.go_to_node(22)
            game.player.drive += 3
        if answer == 'no':
            game.go_to_node(21)

    if current_node.id == 21:
        print(game.player.get_data())
        game.go_to_node(23)

    if current_node.id == 22:
        print(game.player.get_data())
        game.go_to_node(23)

    if current_node.id == 23:
        if answer == 'r':
            game.go_to_node(10)
        if answer == 'x':
            exit()


if __name__ == "__main__":

    default_game = Game()

    while True:
        print(f'\n{default_game.current_node.text}\n')

        if default_game.current_node.answers:
            for answer in default_game.current_node.answers:
                print(answer)

        answer = input('\n> > > ')
        parse_answer(answer.strip().lower(), default_game)
        os.system('cls')
