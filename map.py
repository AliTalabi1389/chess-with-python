_ = False
chess_map = [
    ['r2', 'n2', 'b2', 'k', 'q', 'b1', 'n1', 'r1'],
    ['p8', 'p7', 'p6', 'p5', 'p4', 'p3', 'p2', 'p1'],
    [_, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _],
    ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
    ['R1', 'N1', 'B1', 'Q', 'K', 'B2', 'N2', 'R2']
]

class Map:
    def __init__(self):
        self.map = chess_map
        self.pieces_pos = {}

    def get_map(self):

        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                if cell:
                    self.pieces_pos[i, j] = cell

        return self.pieces_pos
