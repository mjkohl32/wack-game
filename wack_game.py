from wack_interface import *


def play_game():
    """
    Runs the game! Displays the initial interface,
    then assigns a manner of playing (simulation or play
    themselves) and a politician, then plays the game
    based on those parameters. Whether the player chooses
    to play again or quit the game determines whether
    the while loop continues or ends.
    :return: none
    """
    going = True
    while going:
        go = InitialInterface()
        manner = go.select_manner()
        politician = go.select_politician()
        go.close()
        if manner == 'sim':
            game = SimulationInterface(politician)
        else:
            game = GameInterface(politician)
        game.start()
        score = game.play()
        end = FinalInterface(manner, score, politician)
        going = end.close()


def main():
    play_game()


if __name__ == '__main__':
    main()

