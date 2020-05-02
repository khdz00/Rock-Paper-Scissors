#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while (True):
            move = input("Rock, Paper, or Scissors? : ").lower().strip()
            if move == "rock" or move == "paper" or move == "scissors":
                return move


class ReflectPlayer(Player):
    their_move = ""

    def move(self):
        if self.their_move != "":
            return self.their_move
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    my_move = ""

    def move(self):
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        elif self.my_move == "scissors":
            return "rock"
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1_score += 1
            print("Player 1 won!")
        elif beats(move2, move1):
            self.p2_score += 1
            print("Player 2 won!")
        else:
            print("It's a tie!")
        print(f"Score: {self.p1_score}-{self.p2_score}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        print("Best of 3\n")
        for round_num in range(1, 8):
            print(f"Round {round_num}:")
            self.play_round()
            if self.p1_score == 4 or self.p2_score == 4:
                break
        print("Game over!\n")
        if self.p1_score > self.p2_score:
            print("******* Player 1 is the champion *******")
        elif self.p2_score > self.p1_score:
            print("******* Player 2 is the champion *******")
        else:
            print("******* Everyone is a champion *******")


if __name__ == '__main__':
    game = Game(RandomPlayer(), CyclePlayer())
    game.play_game()
