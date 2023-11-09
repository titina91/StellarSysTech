from random import randrange
from time import sleep


class Engine:
    # id increment
    nb_id = 0

    MIN_temperature = 100

    def __init__(self, label="", isp=250, temperature=0, is_on_flag=False):
        # automatically increment id
        Engine.nb_id += randrange(1, 10)

        self.tank = None

        self.id = Engine.nb_id          # id de la fusee
        self.label = label              # le label du moteur
        self.Isp = isp                  # impulsion spécifique d'un moteur
        self.temperature = temperature  # temperature du moteur
        self.is_on_flag = is_on_flag    # moteur allume ou eteint
        self.mass = 1000                # masse du moteur
        self.exit_area = 3              # surface d'échappement
        self.consumption = 0

    def __str__(self):
        attributes = vars(self)
        output = ''
        for attri, value in attributes.items():
            output += f"{attri} : {value} \n"
        return output

    def start_engine(self):
        # if motor is off start it
        self.is_on_flag = self.is_on_flag == False
        burn
        print(f"Engine_id: {self.id} --  warming_up: {self.is_on_flag}")

    def shutdown_engine(self):
        # if motor is turn on then stop it
        self.is_on_flag = ~(self.is_on_flag == True)

    def warm_up(self):
        print(f"warm_up function in engine {self.id}")
        while self.temperature < Engine.MIN_temperature:
            self.temperature += randrange(5, 20)
            print(f"Engine {self.id} temperature : {self.temperature} \n")
            sleep(1)

    def regule_temperature(self):
        while self.temperature > 120:
            print(f"{self.id} is too hot")
            self.temperature -= randrange(1, 5)

    def get_mass_flow_rate(self) -> float:
        return 1000000.0

    def get_exhaust_velocity(self) -> float:
        return 1.0

    def get_exhaust_pressure(self):
        pass

    def run_engine(self):
        self.start_engine()
        self.warm_up()

    def burn(self, consumption):
        while True:
            pass


