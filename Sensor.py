class Sensor:

    def __init__(self, id, name, pos_x, pos_y, pos_z):
        self.id = id
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z

    def __str__(self):
        return f"{self.id}(" \
               f"{self.name}," \
               f"{self.pos_x}," \
               f"{self.pos_y}," \
               f"{self.pos_z})"

    def update(self):
        while(True):
            pass