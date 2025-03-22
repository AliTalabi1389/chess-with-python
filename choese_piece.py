from pgzero.actor import Actor
import pgzrun


class ChosePiece:
    def __init__(self, name=None, image='chose_blank'):
        self.name = name
        self.image = image
        self.define_chose_actor_lock_bool = True

    def define_chose_actor(self):
        if self.define_chose_actor_lock_bool:
            self.name = Actor(self.image, (10000, 10000))
            self.define_chose_actor_lock_bool = False

            return self.name

    def change_position(self):
        self.name.draw()
