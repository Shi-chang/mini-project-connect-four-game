from connect_four import ConnectFour


def main():
    """
    Provide interaction for the game Connect Four
    """
    play_game = ConnectFour()
    print(play_game)
    is_game_over = False
    while not is_game_over:
        user_input = input(f"{play_game.current_player}'s turn. "
                           f"Please choose a column(1-7): ")
        if user_input == "Q":
            print(play_game)
            break
        else:
            play_game.add_piece(int(user_input) - 1)
            print(play_game)

        is_game_over = play_game.is_game_over()

    print("Game Over")
    print(f"Winner is {play_game.get_winner()}")


if __name__ == '__main__':
    main()
