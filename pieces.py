from map import *
from pgzero.actor import Actor
from game import *
from path_finding_actors import *

class Pieces:
    def __init__(self, image=None, position=None, status=None, name=None, type_piece=None, rotation_bool=None, selected_image=None, movement_type=None):
        self.image = image
        self.position = position
        self.status = status
        self.name = name
        self.type_piece = type_piece
        self.pieces_pos = None
        self.actor_define_lock_bool = True
        self.one_piece_pos = ()
        self.arrangement_lock_bool = True
        self.rotation_bool = rotation_bool
        self.selected_image = selected_image
        self.mini_map_pos = ()
        self.movement_type = movement_type

    def define_actor(self):
        if self.actor_define_lock_bool:
            self.name = Actor(self.image)
            self.actor_define_lock_bool = False

            if self.rotation_bool:
                self.name.angle += 180

            return self.name

    def arrangement(self):
        if self.arrangement_lock_bool:
            self.pieces_pos = Map().get_map()
            for pos in self.pieces_pos:
                if self.pieces_pos[pos] == self.type_piece:
                    for i, xy in enumerate(pos):

                        # if i == 1:
                        self.one_piece_pos = self.one_piece_pos +((xy + 1) * 75 + (75 / 2), )

                        # else:
                        #     self.one_piece_pos = self.one_piece_pos + ((xy + 1) * 75 + (75 / 2) - 1, )

                    self.one_piece_pos = self.one_piece_pos[::-1]

                    self.name.pos = self.one_piece_pos

            self.arrangement_lock_bool = False

    def check_click(self, pos):
            if self.name.collidepoint(pos):
                self.name.image = self.selected_image


            else:
                self.name.image = self.image

    def get_mini_map_position(self):
        self.mini_map_pos = ()

        for pos in self.name.pos:
            self.mini_map_pos = self.mini_map_pos + ((pos - (225 / 2)) / 75, )

        return self.mini_map_pos

    def update_piece(self):
        self.define_actor()
        self.arrangement()
        self.get_mini_map_position()

    def draw_piece(self):
        self.name.draw()



class WhiteKing(Pieces):
    def __init__(self, image='white_king', position=None, status='alive', name=None, type_piece='K', rotation_bool=False, selected_image='selected_white_king'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhiteQueen(Pieces):
    def __init__(self, image='white_queen', position=None, status='alive', name=None, type_piece='Q', rotation_bool=False, selected_image='selected_white_queen'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhiteBishop1(Pieces):
    def __init__(self, image='white_bishop', position=None, status='alive', name=None, type_piece='B1', rotation_bool=False, selected_image='selected_white_bishop'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhiteBishop2(Pieces):
    def __init__(self, image='white_bishop', position=None, status='alive', name=None, type_piece='B2', rotation_bool=False, selected_image='selected_white_bishop'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhiteKnight1(Pieces):
    def __init__(self, image='white_knight', position=None, status='alive', name=None, type_piece='N1', rotation_bool=False, selected_image='selected_white_knight'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhiteKnight2(Pieces):
    def __init__(self, image='white_knight', position=None, status='alive', name=None, type_piece='N2', rotation_bool=False, selected_image='selected_white_knight'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhiteRook1(Pieces):
    def __init__(self, image='white_rook', position=None, status='alive', name=None, type_piece='R1', rotation_bool=False, selected_image='selected_white_rook'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhiteRook2(Pieces):
    def __init__(self, image='white_rook', position=None, status='alive', name=None, type_piece='R2', rotation_bool=False, selected_image='selected_white_rook'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhitePawn1(Pieces):
    def __init__(self, image='white_pawn', position=None, status='alive', name=None, type_piece='P1', rotation_bool=False, selected_image='selected_white_pawn', movement_type='pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image, movement_type)

class WhitePawn2(Pieces):
    def __init__(self, image='white_pawn', position=None, status='alive', name=None, type_piece='P2', rotation_bool=False, selected_image='selected_white_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhitePawn3(Pieces):
    def __init__(self, image='white_pawn', position=None, status='alive', name=None, type_piece='P3', rotation_bool=False, selected_image='selected_white_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhitePawn4(Pieces):
    def __init__(self, image='white_pawn', position=None, status='alive', name=None, type_piece='P4', rotation_bool=False, selected_image='selected_white_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhitePawn5(Pieces):
    def __init__(self, image='white_pawn', position=None, status='alive', name=None, type_piece='P5', rotation_bool=False, selected_image='selected_white_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhitePawn6(Pieces):
    def __init__(self, image='white_pawn', position=None, status='alive', name=None, type_piece='P6', rotation_bool=False, selected_image='selected_white_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhitePawn7(Pieces):
    def __init__(self, image='white_pawn', position=None, status='alive', name=None, type_piece='P7', rotation_bool=False, selected_image='selected_white_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class WhitePawn8(Pieces):
    def __init__(self, image='white_pawn', position=None, status='alive', name=None, type_piece='P8', rotation_bool=False, selected_image='selected_white_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackKing(Pieces):
    def __init__(self, image='black_king', position=None, status='alive', name=None, type_piece='k', rotation_bool=False, selected_image='selected_black_king'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackQueen(Pieces):
    def __init__(self, image='black_queen', position=None, status='alive', name=None, type_piece='q', rotation_bool=False, selected_image='selected_black_queen'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackBishop1(Pieces):
    def __init__(self, image='black_bishop', position=None, status='alive', name=None, type_piece='b1', rotation_bool=False, selected_image='selected_black_bishop'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackBishop2(Pieces):
    def __init__(self, image='black_bishop', position=None, status='alive', name=None, type_piece='b2', rotation_bool=False, selected_image='selected_black_bishop'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackKnight1(Pieces):
    def __init__(self, image='black_knight', position=None, status='alive', name=None, type_piece='n1', rotation_bool=False, selected_image='selected_black_knight'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackKnight2(Pieces):
    def __init__(self, image='black_knight', position=None, status='alive', name=None, type_piece='n2', rotation_bool=False, selected_image='selected_black_knight'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackRook1(Pieces):
    def __init__(self, image='black_rook', position=None, status='alive', name=None, type_piece='r1', rotation_bool=False, selected_image='selected_black_rook'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackRook2(Pieces):
    def __init__(self, image='black_rook', position=None, status='alive', name=None, type_piece='r2', rotation_bool=False, selected_image='selected_black_rook'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackPawn1(Pieces):
    def __init__(self, image='black_pawn', position=None, status='alive', name=None, type_piece='p1', rotation_bool=False, selected_image='selected_black_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackPawn2(Pieces):
    def __init__(self, image='black_pawn', position=None, status='alive', name=None, type_piece='p2', rotation_bool=False, selected_image='selected_black_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackPawn3(Pieces):
    def __init__(self, image='black_pawn', position=None, status='alive', name=None, type_piece='p3', rotation_bool=False, selected_image='selected_black_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackPawn4(Pieces):
    def __init__(self, image='black_pawn', position=None, status='alive', name=None, type_piece='p4', rotation_bool=False, selected_image='selected_black_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackPawn5(Pieces):
    def __init__(self, image='black_pawn', position=None, status='alive', name=None, type_piece='p5', rotation_bool=False, selected_image='selected_black_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackPawn6(Pieces):
    def __init__(self, image='black_pawn', position=None, status='alive', name=None, type_piece='p6', rotation_bool=False, selected_image='selected_black_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackPawn7(Pieces):
    def __init__(self, image='black_pawn', position=None, status='alive', name=None, type_piece='p7', rotation_bool=False, selected_image='selected_black_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)

class BlackPawn8(Pieces):
    def __init__(self, image='black_pawn', position=None, status='alive', name=None, type_piece='p8', rotation_bool=False, selected_image='selected_black_pawn'):
        super().__init__(image, position, status, name, type_piece, rotation_bool, selected_image)
