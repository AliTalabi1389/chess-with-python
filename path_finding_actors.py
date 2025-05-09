from pgzero.actor import Actor


class PathActors:
    def __init__(self, x, y):
        self.image = 'null'
        self.x = x
        self.y = y
        self.path_actor_define_lock_bool = True
        self.arrangement_lock_bool = True
        self.name = None

    def define_path_actor(self):
        if self.path_actor_define_lock_bool:
            self.name = Actor(self.image)
            self.path_actor_define_lock_bool = False


    def arrangement(self):
        if self.arrangement_lock_bool:
            self.name.pos = ((self.x + 1) * 75 + (75 / 2), (self.y + 1) * 75 + (75 / 2))
            self.arrangement_lock_bool = False

    def hide_path(self):
        self.name.pos = (10000, 10000)

    def show_path(self):
        pass

    def update_path(self):
        self.define_path_actor()
        self.arrangement()

    def draw_path(self):
        self.name.draw()


class PathActor1(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor2(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor3(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor4(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor5(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor6(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor7(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor8(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor9(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor10(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor11(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor12(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor13(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor14(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor15(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor16(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor17(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor18(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor19(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor20(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor21(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor22(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor23(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor24(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor25(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor26(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor27(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor28(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor29(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor30(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor31(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor32(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor33(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor34(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor35(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor36(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor37(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor38(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor39(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor40(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor41(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor42(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor43(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor44(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor45(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor46(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor47(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor48(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor49(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor50(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor51(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor52(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor53(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor54(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor55(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor56(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor57(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor58(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor59(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor60(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor61(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor62(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor63(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)

class PathActor64(PathActors):
    def __init__(self, x, y):
        super().__init__(x, y)