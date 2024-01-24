from random import randrange
from time import sleep

import threading
import Tank
import logging

START_CONSUMPTION = 2  # consommation par unité de temps lorsque le moteur est juste allumé
BURN_CONSUMPTION = 5  # consommation par unité de temps lorsque le moteur est à plein régime
TEMPERATURE_MAX = 800  # température max
TEMPERATURE_MIN = 100  # température min

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Engine:
    # id increment
    nb_id = 0

    def __init__(self,
                 label: str = "",
                 specific_impulse: int = 250,
                 temperature: float = 20,
                 is_on_flag: bool = False,
                 associated_tank: Tank.Tank = None):

        # automatically increment id
        Engine.nb_id += randrange(1, 10)

        self.id = Engine.nb_id  # id de la fusee
        self.label = label  # le label du moteur
        self.specific_impulse = specific_impulse  # impulsion spécifique d'un moteur
        self.temperature = temperature  # temperature du moteur
        self._mass = 1000  # masse du moteur
        self._exit_area = 3  # surface d'échappement
        self.consumption = 0
        self.engine_power = 1.0

        self.logger = logging.getLogger(f"-- Engine--{self.id} : ")
        self.associated_tank = associated_tank

        # flag use for control
        self.is_on_flag = is_on_flag  # moteur allume ou eteint

        # thread deamon qui permet de réguler la température du moteur
        self.temperatureThread = threading.Thread(target=self.control_temperature)
        self.temperatureThread.daemon = True

        # thread deamon qui permet de gérer la combustion du moteur
        self.burnThread = threading.Thread(target=self.burn)
        self.burnThread.daemon = True

        self.start_engine()

    def __str__(self):
        attributes = vars(self)
        output = ''
        for attribute, value in attributes.items():
            output += f"{attribute} : {value} \n"
        return output

    def control_temperature(self):
        try:
            while True:
                if TEMPERATURE_MIN <= self.temperature < TEMPERATURE_MAX:
                    self.temperature -= randrange(1, 5)
                    sleep(10)
                elif self.temperature >= TEMPERATURE_MAX:
                    logger.warning(f"{self.id} is too hot")
                    self.temperature -= randrange(1, 5)
                    sleep(20)
                elif not self.has_enough_fuel():
                    break
        except Exception as e:
            self.logger.error(f"An error occurred in control_temperature: {e}")

    def burn(self):
        try:
            while self.has_enough_fuel():
                self.associated_tank.fuel -= self.consumption
                self.temperature += randrange(1, 20)
                sleep(0.1)
            if self.associated_tank.fuel > 0:
                self.consumption = round(0.5 * self.consumption)
                self.burn()
                self.shutdown_engine()
        except Exception as e:
            self.logger.error(f"An error occurred in burn: {e}")

    def start_engine(self):
        self.consumption = START_CONSUMPTION
        self.is_on_flag = True
        self.burnThread.start()
        self.temperatureThread.start()

    def shutdown_engine(self):
        # if motor is turn on then stop it
        self.is_on_flag = False

    def get_mass_flow_rate(self) -> float:
        pass

    def get_exhaust_velocity(self) -> float:
        pass

    def get_exhaust_pressure(self):
        pass

    def has_enough_fuel(self):
        return self.associated_tank.fuel - self.consumption >= 0

    def get_exit_area(self):
        return self._exit_area
