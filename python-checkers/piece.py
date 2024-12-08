from utils import get_position_with_row_col

class Piece:
    def __init__(self, name):
        # Example: <position><color><isKing?> 16WN
        self.name = name
        self.has_eaten = False # True if the piece instance has eaten a piece in its last move
    
    def get_name(self):
        return self.name

    def get_position(self):
        return self.name[:-2]

    def get_color(self):
        return self.name[-2]
    
    def get_has_eaten(self):
        return self.has_eaten

    def is_king(self):
        return True if self.name[-1] == 'Y' else False
    
    def set_position(self, new_position):
        # Receives a new position and assigns it.
        # position_index is used because the position part of self.name can be a one or two digit number. 
        position_index = 1 if len(self.name) == 3 else 2
        self.name = str(new_position) + self.name[position_index:]
    
    def set_is_king(self, new_is_king):
        is_king = "Y" if new_is_king else "N"
        self.name = self.name[:-1] + is_king

    def set_has_eaten(self, has_eaten):
        self.has_eaten = has_eaten

    def get_adjacent_squares(self, board):
        current_row = board.get_row_number(int(self.get_position()))
        current_col = board.get_col_number(int(self.get_position()))

        adjacent_squares = []
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Diagonais
            new_row, new_col = current_row + dr, current_col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:  # Dentro do tabuleiro
                adjacent_squares.append((new_row, new_col))

        return adjacent_squares


    def get_moves(self, board):
        # Receives a board, returns all possible moves.
        def get_eat_position(piece, coords):
            # Receives a piece that is obstructing this piece's way and its (row, column) coordinates.
            # Returns the position to move in order to eat the piece, or None if it's impossible.
            if (piece.get_color() == own_color) or (coords[0] in (0, 7)) or (coords[1] in (0, 7)):
                return None

            if coords[1] > current_col:
                # (coords[0] - current_row) returns 1 if the target is below this piece, and -1 otherwise.
                position_to_eat = (coords[0] + (coords[0] - current_row), coords[1] + 1)
            else:
                position_to_eat = (coords[0] + (coords[0] - current_row), coords[1] - 1)

            position_num = get_position_with_row_col(position_to_eat[0], position_to_eat[1])

            return None if board.has_piece(position_num) else position_num

        current_col = board.get_col_number(int(self.get_position()))
        current_row = board.get_row_number(int(self.get_position()))
        possible_moves = []
        own_color = self.get_color()

        possible_coords = self.get_adjacent_squares(board)

        # Get pieces in adjacent squares
        close_squares = board.get_pieces_by_coords(*possible_coords)
        empty_squares = []

        for index, square in enumerate(close_squares):
            # Empty squares are potential moves. Pieces are potential eating movements.
            if square is None:
                empty_squares.append(index)
            else:
                position_to_eat = get_eat_position(square, possible_coords[index])
                if position_to_eat is None:
                    continue

                possible_moves.append({"position": str(position_to_eat), "eats_piece": True})

        # Filter empty_squares to avoid out-of-range access
        empty_squares = [index for index in empty_squares if index < len(possible_coords)]

        if len(possible_moves) == 0:
            # This is skipped if this piece can eat any other, because it is forced to eat it.
            for index in empty_squares:
                # Ensure the index is valid before accessing
                if index < len(possible_coords):
                    new_position = get_position_with_row_col(possible_coords[index][0], possible_coords[index][1])
                    possible_moves.append({"position": str(new_position), "eats_piece": False})

        return possible_moves
