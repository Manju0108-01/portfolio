import random


class Dice:
    def __init__(self, dice_size=6):
        self.dice_size = dice_size * 6

    def roll_dice(self):
        return random.randint(1, self.dice_size)


class Ladder:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top


class Snake:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


class Player:
    def __init__(self, player_id, player_name):
        self.player_id = player_id
        self.player_name = player_name
        self.player_position = 0

    def get_player_id(self):
        return self.player_id

    def get_player_name(self):
        return self.player_name

    def get_player_position(self):
        return self.player_position

    def set_player_position(self, player_position):
        self.player_position = player_position


class Board:
    def __init__(self, board_size=100, no_of_dice=1):
        self.board_size = board_size
        self.no_of_dice = no_of_dice
        self.players = []
        self.snakes = {}
        self.ladders = {}

    def set_players(self, players):
        self.players = players

    def set_snakes(self, snakes):
        self.snakes = snakes

    def set_ladders(self, ladders):
        self.ladders = ladders

    def play(self):
        is_won = False
        while True:
            current_player = self.players.pop(0)
            print("\n" + current_player.get_player_name() + "!, It's your turn....")
            dice = Dice(self.no_of_dice)

            while True:
                is_roll = input("\nEnter '1' to play: ")
                if is_roll == '1':
                    current_position = current_player.get_player_position()
                    dice_value = dice.roll_dice()
                    print(current_player.get_player_name() + ", You rolled " + str(dice_value))
                    new_position = current_position + dice_value

                    if new_position <= self.board_size:
                        if new_position in self.snakes:
                            print("Oops!, You've been swallowed by a Snake")
                            new_position = self.snakes[new_position].tail

                        if new_position in self.ladders:
                            print("Wow!, You climbed the Ladder and get an extra turn...")
                            new_position = self.ladders[new_position].top
                            current_position = new_position
                            current_player.set_player_position(current_position)
                            continue

                        current_position = new_position
                        print(current_player.get_player_name() + " moved to " + str(current_position))

                        if current_position == self.board_size:
                            print("\nCongrats " + current_player.get_player_name() + "!, you won the game....")
                            is_won = True
                            break

                        current_player.set_player_position(current_position)

                        if dice_value != 6:
                            break
                        else:
                            print("As you rolled 6, you get an extra turn...")

                    else:
                        break

            if is_won:
                break

            self.players.append(current_player)


if __name__ == "__main__":
    print("Hello User....")
    wants_to_play = input("Do you want to play the Snake and Ladders?(Y/N)").upper()

    if wants_to_play == "Y":
        print("......................Welcome to Snake and Ladders......................")
        no_of_players = int(input("\nEnter the number of Players : "))
        players = []

        for i in range(1, no_of_players + 1):
            player_name = input("\nEnter the player " + str(i) + " name : ")
            player = Player(i, player_name)
            players.append(player)

        board_size = int(input("\nEnter the Board Size : "))
        no_of_dice = int(input("\nEnter the Number of the Die you want to use : "))

        no_of_snakes = int(input("\nEnter the Number of Snakes : "))
        snakes = {}
        if no_of_snakes != 0:
            print("\nEnter the Head and Tail positions of each Snake :")
            i = 0
            while i < no_of_snakes:
                head = int(input())
                tail = int(input())
                if head == board_size:
                    print("!!Snake should not be present at the Destination!!")
                    print("Please Enter a valid head position...")
                    continue
                if head > board_size or tail > board_size or head < 1 or tail < 1:
                    print("!!Please Enter valid positions from 1 to " + str(board_size) + "!!")
                    continue
                snake = Snake(head, tail)
                snakes[head] = snake
                i += 1

        no_of_ladders = int(input("\nEnter the Number of Ladders : "))
        ladders = {}
        if no_of_ladders != 0:
            print("Enter the Initial and Final positions of each ladder :")
            i = 0
            while i < no_of_ladders:
                bottom = int(input())
                top = int(input())
                if top in snakes or bottom in snakes:
                    print("!!Ladder ends should not be present at the Snake's head!!")
                    print("Please Enter a valid Ladder position...")
                    continue
                if top == board_size:
                    print("!!Ladder's end should not be present at the Destination!!")
                    print("Please Enter a valid Ladder position...")
                    continue
                if top > board_size or bottom > board_size or top < 1 or bottom < 1:
                    print("!!Please Enter valid positions from 1 to " + str(board_size) + "!!")
                    continue
                ladder = Ladder(bottom, top)
                ladders[bottom] = ladder
                i += 1

        game_board = Board(board_size, no_of_dice)
        game_board.set_players(players)
        game_board.set_ladders(ladders)
        game_board.set_snakes(snakes)

        print("......................Let's Play......................")
        game_board.play()

    else:
        print("No problem, let me know if you change your mind")
