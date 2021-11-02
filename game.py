
import random
import os


class Game:

    def __init__(self):
        self.player1 = "X"
        self.player2 = "O"
        self.number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.win_and_lost = ""
        self.draw = ""
        self.busy_x = []

    def players(self):
        self.clear()
        chose = input("computer --> [1] or you --> [2], choose: ")
        if chose == '2':
            self.clear()
            self.show_game()
            o = input("player2: ").strip()
            while not o.isdigit() or o in self.busy_x:
                self.clear()
                print("Error pleas try again: ")
                o = input("player2: ").strip()
            self.check(o, self.player2)
            self.show_game()
            self.computer()
        else:
            self.computer()

    def computer(self):
        self.clear()
        self.show_game()
        while True:
            x = random.choice(self.number)
            while not x.isdigit():
                x = random.choice(self.number)
            self.check(x, self.player1)
            self.busy_x.append(x)
            if self.win_and_lost:
                break
            elif self.draw:
                print("The match ended in a draw")
                break

            o = input("player2: ").strip()
            while not o.isdigit() or o in self.busy_x:
                self.clear()
                print("Error pleas try again: ")
                o = input("player2: ").strip()
            self.check(o, self.player2)
            if self.win_and_lost:
                break
            elif self.draw:
                print("The match ended in a draw")
                break

    def show_game(self):
        b, a, c, d, f, g, h, i, k, = self.number
        print(f"""
        | {b} |  {a} | {c} |
        | {d} |  {f} | {g} |
        | {h} |  {i} | {k} |
        """)
        self.check_win(b, a, c, d, f, g, h, i, k)

    def check(self, check_num, player):
        for i in range(len(self.number)):
            if self.number[i] == check_num:
                self.number[i] = player

        self.clear()
        self.show_game()

    @staticmethod
    def clear():
        os.system("clear")

    def check_win(self, b, a, c, d, f, g, h, i, k):
        if b == 'X' and d == 'X' and h == 'X':
            print("Player1  win")
            self.win_and_lost = 'X'
        elif b == 'O' and d == 'O' and h == 'O':
            print("Player2  win")
            self.win_and_lost = 'O'

        elif a == 'X' and f == 'X' and i == 'X':
            print("Player1  win")
            self.win_and_lost = 'X'
        elif a == 'O' and f == 'O' and i == 'O':
            print("Player2  win")
            self.win_and_lost = 'O'

        elif c == 'X' and g == 'X' and k == 'X':
            print("Player1  win")
            self.win_and_lost = 'X'
        elif c == 'O' and g == 'O' and k == 'O':
            print("Player2  win")
            self.win_and_lost = 'O'

        elif b == 'X' and a == 'X' and c == 'X':
            print("Player1  win")
            self.win_and_lost = 'X'
        elif b == 'O' and a == 'O' and c == 'O':
            print("Player2  win")
            self.win_and_lost = 'O'

        elif d == 'X' and f == 'X' and g == 'X':
            print("Player1  win")
            self.win_and_lost = 'X'
        elif d == 'O' and f == 'O' and g == 'O':
            print("Player2  win")
            self.win_and_lost = 'O'

        elif h == 'X' and i == 'X' and k == 'X':
            print("Player1  win")
            self.win_and_lost = 'X'
        elif h == 'O' and i == 'O' and k == 'O':
            print("Player2  win")
            self.win_and_lost = 'O'

        elif b == 'X' and f == 'X' and k == 'X':
            print("Player1  win")
            self.win_and_lost = 'X'
        elif b == 'O' and f == 'O' and k == 'O':
            print("Player2  win")
            self.win_and_lost = 'O'

        elif c == 'X' and f == 'X' and h == 'X':
            print("Player1  win")
            self.win_and_lost = 'X'
        elif c == 'O' and f == 'O' and h == 'O':
            print("Player2  win")
            self.win_and_lost = 'O'
        else:
            self.lol()

    def lol(self):
        self.draw = "".join(self.number)
        if self.draw.isalpha():
            self.draw = 'd'
        else:
            self.draw = None


result = Game()
result.players()
