import unittest
from collections import deque
from connect_four import ConnectFour


# This class conducts unitests for the class ConnectFour
class ConnectFourTest(unittest.TestCase):
    def test_init(self):
        """
        Test the initialization of objects
        """
        game_play = ConnectFour()
        self.assertEqual(game_play.board,
                         [[" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "]])
        self.assertEqual(game_play.current_location, [-1, -1])
        self.assertEqual(game_play.store_moves, [])
        self.assertEqual(game_play.players, deque(["O", "X"]))
        self.assertEqual(game_play.current_player, "X")

    def test_whose_turn(self):
        """
        Test the function whose_turn
        """
        game_play = ConnectFour()
        game_play.whose_turn()
        self.assertEqual(game_play.current_player, "O")
        self.assertEqual(game_play.players, deque(["X", "O"]))

    def test_add_piece(self):
        """
        Test the function add_piece
        """
        game_play = ConnectFour()
        self.assertRaises(ValueError, game_play.add_piece, -1)

        game_play.board = [["X", " ", " ", " ", " ", " ", " "],
                           ["O", " ", " ", " ", " ", " ", " "],
                           ["O", " ", " ", " ", " ", " ", " "],
                           ["O", " ", " ", " ", " ", " ", " "],
                           ["X", " ", " ", " ", " ", " ", " "],
                           ["X", " ", " ", " ", " ", " ", " "]]
        self.assertRaises(ValueError, game_play.add_piece, 0)

        game_play.board = [[" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "]]
        game_play.current_player = "X"
        game_play.add_piece(0)
        self.assertRaises(ValueError, game_play.add_piece, 1)

        game_play.board = [[" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "]]
        game_play.current_player = "X"
        game_play.add_piece(0)
        expected_result = [[" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           ["X", " ", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "]]
        self.assertEqual(game_play.board, expected_result)

    def test_is_board_full(self):
        """
        Test the function is_board_full
        """
        game_play = ConnectFour()
        # The board is full
        game_play.board = [["O", "O", "O", "X", "X", "X", "O"],
                           ["O", "O", "O", "X", "X", "X", "O"],
                           ["O", "O", "O", "X", "X", "X", "O"],
                           ["X", "X", "X", "O", "O", "O", "X"],
                           ["X", "X", "X", "O", "O", "O", "X"],
                           ["X", "X", "X", "O", "O", "O", "X"]]
        self.assertEqual(game_play.is_board_full(), True)

        # The board is not full
        game_play.board = [["O", "O", " ", "X", "X", "X", "O"],
                           ["O", "O", "O", "X", "X", "X", "O"],
                           ["O", "O", "O", "X", "X", "X", "O"],
                           ["X", "X", "X", "O", "O", "O", "X"],
                           ["X", "X", "X", "O", "O", "O", "X"],
                           ["X", "X", "X", "O", "O", "O", "X"]]
        self.assertEqual(game_play.is_board_full(), False)

    def test_player_connect_four(self):
        """
        Test the function player_connect_four
        """
        #
        game_play = ConnectFour()
        # Four pieces connected vertically
        game_play.board = [[" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "]]
        game_play.current_player = "X"
        game_play.add_piece(0)
        self.assertEqual(game_play.player_connect_four(), "X")

        # Four pieces connected horizontally
        game_play.board = [[" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           ["X", " ", " ", " ", " ", " ", " "],
                           ["X", "X", "X", " ", " ", " ", " "],
                           ["X", "O", "O", "O", " ", " ", " "]]
        game_play.current_player = "O"
        game_play.add_piece(4)
        self.assertEqual(game_play.player_connect_four(), "O")

        # No four pieces connected
        game_play.board = [[" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           ["X", " ", " ", " ", " ", " ", " "],
                           ["X", "X", "X", " ", " ", " ", " "],
                           ["X", "O", "O", "O", " ", " ", " "]]
        game_play.current_player = "O"
        game_play.add_piece(5)
        self.assertEqual(game_play.player_connect_four(), None)

        # Four pieces connected diagonally
        game_play.board = [[" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", "O", "O", "X", " "],
                           ["X", "X", "X", "O", "X", "X", " "],
                           ["X", "O", "O", "O", "X", "O", " "]]
        game_play.current_player = "O"
        game_play.add_piece(5)
        self.assertEqual(game_play.player_connect_four(), "O")

        # Four pieces connected diagonally
        game_play.board = [[" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", "O", "X", "O", "O", "X", " "],
                           ["O", "O", "X", "X", "X", "X", " "],
                           ["X", "O", "O", "O", "X", "O", " "]]
        game_play.current_player = "X"
        game_play.add_piece(1)
        self.assertEqual(game_play.player_connect_four(), "X")

    def test_is_game_over(self):
        """
        Test the function is_game_over
        :return:
        """
        game_play = ConnectFour()
        # Game is over with one player's four pieces connected
        game_play.board = [[" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "]]
        game_play.current_player = "X"
        game_play.add_piece(0)
        self.assertEqual(game_play.is_game_over(), True)

        # Game is over when the board is full
        game_play.board = [["O", "O", " ", "X", "X", "X", "O"],
                           ["O", "O", "O", "X", "X", "X", "O"],
                           ["O", "O", "O", "X", "X", "X", "O"],
                           ["X", "X", "X", "O", "O", "O", "X"],
                           ["X", "X", "X", "O", "O", "O", "X"],
                           ["X", "X", "X", "O", "O", "O", "X"]]
        game_play.current_player = "O"
        game_play.add_piece(2)
        self.assertEqual(game_play.is_game_over(), True)

    def test_get_winner(self):
        """
        Test the function get_Winner
        """
        game_play = ConnectFour()
        game_play.board = [[" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "],
                           ["X", "O", " ", " ", " ", " ", " "]]
        game_play.current_player = "X"
        game_play.add_piece(0)
        self.assertEqual(game_play.player_connect_four(), "X")

    def test_undo(self):
        """
        Test the function undo
        """
        game_play = ConnectFour()
        game_play.add_piece(0)
        game_play.add_piece(1)
        game_play.add_piece(0)
        game_play.add_piece(1)
        game_play.add_piece(0)
        game_play.add_piece(1)

        # remove the last piece
        game_play.undo()
        expected_board = [[" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          ["X", " ", " ", " ", " ", " ", " "],
                          ["X", "O", " ", " ", " ", " ", " "],
                          ["X", "O", " ", " ", " ", " ", " "]]
        self.assertEqual(game_play.board, expected_board)
        # remove the second to last piece
        game_play.undo()
        expected_board = [[" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          ["X", "O", " ", " ", " ", " ", " "],
                          ["X", "O", " ", " ", " ", " ", " "]]
        self.assertEqual(game_play.board, expected_board)
        # remove the third to last piece
        game_play.undo()
        expected_board = [[" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          ["X", " ", " ", " ", " ", " ", " "],
                          ["X", "O", " ", " ", " ", " ", " "]]
        self.assertEqual(game_play.board, expected_board)

    def test_str(self):
        """
        Test the function __str__
        """
        game_play = ConnectFour()
        game_play.add_piece(0)
        game_play.add_piece(1)
        game_play.add_piece(0)
        game_play.add_piece(1)
        game_play.add_piece(0)
        game_play.add_piece(1)
        expected_board = "| | | | | | | |\n" \
                         "---------------\n" \
                         "| | | | | | | |\n" \
                         "---------------\n" \
                         "| | | | | | | |\n" \
                         "---------------\n" \
                         "|X|O| | | | | |\n" \
                         "---------------\n" \
                         "|X|O| | | | | |\n" \
                         "---------------\n" \
                         "|X|O| | | | | |\n" \
                         "---------------\n"
        self.assertEqual(game_play.__str__(), expected_board)


if __name__ == '__main__':
    unittest.main()

main()
