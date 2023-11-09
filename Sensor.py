from time import sleep

class Sensor:

    # id increment
    nb_id = 0

    def __init__(self, label, pos_x, pos_y, pos_z):

        # automatically increment id
        Sensor.nb_id += 1

        self.id = Sensor.nb_id
        self.label = label
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z

    def __str__(self):
        return f"{self.id}(" \
               f"{self.label}," \
               f"{self.pos_x}," \
               f"{self.pos_y}," \
               f"{self.pos_z})"

    def update(self, new_x, new_y, new_z):
        while(True):
            self.pos_x, self.pos_y, self.pos_z = new_x, new_y, new_z