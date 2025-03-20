from pieces import *

class Game:
    def __init__(self):
        self.wk = WhiteKing()
        self.wq = WhiteQueen()
        self.wb1 = WhiteBishop1()
        self.wb2 = WhiteBishop2()
        self.wn1 = WhiteKnight1()
        self.wn2 = WhiteKnight2()
        self.wr1 = WhiteRook1()
        self.wr2 = WhiteRook2()
        self.wp1 = WhitePawn1()
        self.wp2 = WhitePawn2()
        self.wp3 = WhitePawn3()
        self.wp4 = WhitePawn4()
        self.wp5 = WhitePawn5()
        self.wp6 = WhitePawn6()
        self.wp7 = WhitePawn7()
        self.wp8 = WhitePawn8()
        self.bk = BlackKing()
        self.bq = BlackQueen()
        self.bb1 = BlackBishop1()
        self.bb2 = BlackBishop2()
        self.bn1 = BlackKnight1()
        self.bn2 = BlackKnight2()
        self.br1 = BlackRook1()
        self.br2 = BlackRook2()
        self.bp1 = BlackPawn1()
        self.bp2 = BlackPawn2()
        self.bp3 = BlackPawn3()
        self.bp4 = BlackPawn4()
        self.bp5 = BlackPawn5()
        self.bp6 = BlackPawn6()
        self.bp7 = BlackPawn7()
        self.bp8 = BlackPawn8()

    def draw(self):
        self.wk.draw_piece()
        self.wq.draw_piece()
        self.wb1.draw_piece()
        self.wb2.draw_piece()
        self.wn1.draw_piece()
        self.wn2.draw_piece()
        self.wr1.draw_piece()
        self.wr2.draw_piece()
        self.wp1.draw_piece()
        self.wp2.draw_piece()
        self.wp3.draw_piece()
        self.wp4.draw_piece()
        self.wp5.draw_piece()
        self.wp6.draw_piece()
        self.wp7.draw_piece()
        self.wp8.draw_piece()
        self.bk.draw_piece()
        self.bq.draw_piece()
        self.bb1.draw_piece()
        self.bb2.draw_piece()
        self.bn1.draw_piece()
        self.bn2.draw_piece()
        self.br1.draw_piece()
        self.br2.draw_piece()
        self.bp1.draw_piece()
        self.bp2.draw_piece()
        self.bp3.draw_piece()
        self.bp4.draw_piece()
        self.bp5.draw_piece()
        self.bp6.draw_piece()
        self.bp7.draw_piece()
        self.bp8.draw_piece()

    def update(self):
        self.wk.update_piece()
        self.wq.update_piece()
        self.wb1.update_piece()
        self.wb2.update_piece()
        self.wn1.update_piece()
        self.wn2.update_piece()
        self.wr1.update_piece()
        self.wr2.update_piece()
        self.wp1.update_piece()
        self.wp2.update_piece()
        self.wp3.update_piece()
        self.wp4.update_piece()
        self.wp5.update_piece()
        self.wp6.update_piece()
        self.wp7.update_piece()
        self.wp8.update_piece()
        self.bk.update_piece()
        self.bq.update_piece()
        self.bb1.update_piece()
        self.bb2.update_piece()
        self.bn1.update_piece()
        self.bn2.update_piece()
        self.br1.update_piece()
        self.br2.update_piece()
        self.bp1.update_piece()
        self.bp2.update_piece()
        self.bp3.update_piece()
        self.bp4.update_piece()
        self.bp5.update_piece()
        self.bp6.update_piece()
        self.bp7.update_piece()
        self.bp8.update_piece()

    def check_mouse_down(self, pos):
        self.wk.check_click(pos)
        self.wq.check_click(pos)
        self.wb1.check_click(pos)
        self.wb2.check_click(pos)
        self.wn1.check_click(pos)
        self.wn2.check_click(pos)
        self.wr1.check_click(pos)
        self.wr2.check_click(pos)
        self.wp1.check_click(pos)
        self.wp2.check_click(pos)
        self.wp3.check_click(pos)
        self.wp4.check_click(pos)
        self.wp5.check_click(pos)
        self.wp6.check_click(pos)
        self.wp7.check_click(pos)
        self.wp8.check_click(pos)
        self.bk.check_click(pos)
        self.bq.check_click(pos)
        self.bb1.check_click(pos)
        self.bb2.check_click(pos)
        self.bn1.check_click(pos)
        self.bn2.check_click(pos)
        self.br1.check_click(pos)
        self.br2.check_click(pos)
        self.bp1.check_click(pos)
        self.bp2.check_click(pos)
        self.bp3.check_click(pos)
        self.bp4.check_click(pos)
        self.bp5.check_click(pos)
        self.bp6.check_click(pos)
        self.bp7.check_click(pos)
        self.bp8.check_click(pos)