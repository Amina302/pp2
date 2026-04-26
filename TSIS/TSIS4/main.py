import pygame
from game import SnakeGame

def get_username():
    return input("Enter username: ")

def main():
    username = get_username()
    game = SnakeGame(username)
    game.run()

if __name__ == "__main__":
    main()