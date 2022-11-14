class Board:
    def __init__(self) -> None:
        pass

    def display_board(self) -> None:
        pass

    def make_move(self, move, player) -> None:
        pass

    def check_win(self, player) -> bool:
        return False

    def is_draw(self) -> bool:
        return False


class Player:
    def __init__(self, board) -> None:
        self.player_board = board

    def get_move(self) -> tuple[int, int]:
        raise
        return 0,0


class HumanPlayer(Player):
    pass


class AIPlayer(Player):
    pass


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.players = [HumanPlayer(self.board), AIPlayer(self.board)]
        self.player_index = 0

    def play(self) -> None:
        while True:
            # Display the current board state
            self.board.display_board()

            # For convenience, store the current player
            current_player = self.players[self.player_index]

            # Get a move. This will call different methods depending on the type of Player
            move = current_player.get_move()
            self.board.make_move(move, current_player)

            # Check if the current player has won
            if self.board.check_win(current_player):
                print(f'The winner is {current_player.get_name()}')
                break
            elif self.board.is_draw():
                print("It's a draw")
                break

            # Swap to the other player, ready for the next iteration
            if self.player_index == 1:
                self.player_index = 0
            else:
                self.player_index = 1



if __name__ == "__main__":
    game = Game()
    game.play()
