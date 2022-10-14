from collections import deque


# This class creates a Connect Four game where the player("X" or "O")
# who connects four of their pieces in a row wins.
class ConnectFour:
    def __init__(self):
        """
        Initialize the object
        """
        self.board = [[" " for i in range(7)] for j in range(6)]
        self.current_location = [-1, -1]
        self.store_moves = []
        self.players = deque(["O", "X"])
        self.current_player = "X"

    def whose_turn(self):
        """
        Alternate between two players everytime this function is called
        """
        self.current_player = self.players.popleft()
        self.players.append(self.current_player)

    def add_piece(self, column):
        """
        Put the current player's piece to the lowest row of the column
        :param column: the column to put the piece
        :return: the location of thea added piece
        """
        if column < 0 or column > 7:
            raise ValueError("Column outside of the playing area!")
        elif self.board[0][column] != " ":
            raise ValueError("The selected column is already full!")
        elif self.is_game_over():
            raise ValueError("The game is already over!")
        for r in range(5, -1, -1):
            if self.board[r][column] == " ":
                self.board[r][column] = self.current_player
                self.whose_turn()
                self.current_location = [r, column]
                self.store_moves.append([r, column])
                break
        return self.current_location

    def is_board_full(self):
        """
        Check if the board is already full
        :return: True if the board is full or False if it is not
        """
        is_full = True
        # Check if the top row is full
        for c in self.board[0]:
            if c == " ":
                is_full = False
                break
        return is_full

    def player_connect_four(self):
        """
        Check if the current player successfully connects fours pieces
        in a row
        :return: the player's symbol("X" or "O") if four pieces are
                 connected or None if no fours pieces are connected
        """
        current_row = self.current_location[0]
        current_column = self.current_location[1]
        current_player = self.board[current_row][current_column]

        # Directions for up & down, left & right, up-left & bottom-right,
        # up-right & bottom-left. Each direction pair may connect pieces.
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1),
                      (1, 1), (-1, 1), (1, -1)]
        # Record the number of pieces around the current player that are
        # connected in every direction
        direction_length = [0 for d in directions]
        # Check if the surrounding spaces(3 steps in horizontal, vertical
        # and diagonal directions) are occupied by the same player
        for d in directions:
            for i in range(4):
                extended_row = current_row + d[0] * (i + 1)
                extended_column = current_column + d[1] * (i + 1)
                # Make sure that the extended location is within the limit
                if 0 <= extended_row < 6 and 0 <= extended_column < 7:
                    if self.board[extended_row][extended_column] \
                            == current_player and \
                            self.board[extended_row][extended_column] != " ":
                        direction_length[directions.index(d)] += 1
                    else:
                        break
        # Check if in any direction pair(horizontal, vertical and diagonal
        # the current player's at least four pieces are connected
        for i in range(0, 7, 2):
            if direction_length[i] + direction_length[i + 1] >= 3:
                return current_player
        return None

    def is_game_over(self):
        """
        Check if the game is over
        :return: True is the game if the game is over
        """
        if self.player_connect_four() or self.is_board_full():
            return True

    def get_winner(self):
        """
        Get the player who connects four pieces in a row
        :return: the winner's symbol("X" or "O") if there is a
                 winner or None if there is no winner
        """
        if self.player_connect_four():
            return self.player_connect_four()
        else:
            return None

    def undo(self):
        """
        Remove the last pieces that was put by the last player
        """
        if self.store_moves == []:
            raise ValueError("pop from empty list")
        else:
            popped_location = self.store_moves.pop()
            self.board[popped_location[0]][popped_location[1]] = " "

    def __str__(self):
        """
        Create a string that represents that board
        :return: the string
        """
        self.board_string = ""
        for r in range(6):
            self.board_string += "|"
            for c in range(7):
                self.board_string += f"{self.board[r][c]}|"
            self.board_string += "\n"
            self.board_string += "-" * 15 + "\n"
        return self.board_string
