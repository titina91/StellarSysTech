from time import time
from Engine import Engine

import Tank as tank
import multiprocessing
import copy


class Stage:
    # id increment
    nb_id = 0

    def __init__(self,
                 label="",
                 status='OFF',
                 nb_engine=0,
                 empty_weight=1000,
                 burn_time=300,
                 max_thrust=2000,
                 fuel_consumption_rate=0):

        # automatically increment id
        Stage.nb_id += 1  # increment de la class

        self.id = Stage.nb_id  # identifiant de l'etage
        self.label = label  # label associé à l'etage
        self.status = status  # statu de l'etage
        self.nb_engine = nb_engine  # nombre de monteur
        self.empty_weight = empty_weight  # masse de l'étage
        self.burn_time = burn_time  # durée de combustion
        self.max_thrust = max_thrust  # poussée maximum
        self.fuel_consumption_rate = fuel_consumption_rate  # consomation de carburant en kg/s

        # object relation
        self.tank = tank.Tank()  # réservoir de l'étage
        self.engines = {}  # ensemble des moteurs

        # own variables
        self.start_time = None
        self._thrust = 0
        self._mass = copy.copy(self.empty_weight)

    """ Getter et Setter"""

    @property
    def thrust(self):
        return self._thrust

    @thrust.setter
    def thrust(self, value):
        if value > 0:
            self._thrust = value
        else:
            raise ValueError("La poussé calculé est négative")

    @property
    def mass(self):
        return self.empty_weight + sum([engine.mass for engine in self.engines])

    def __str__(self):
        return f"""
                Stage ID  : {self.id}
                Label     : {self.label}
                Status    : {self.status}
                Nb engine : {len(self.engines)}
                """

    def add_engine(self, engine: Engine) -> None:
        self.engines.add(engine)
        self.mass(engine)
        self.nb_engine += 1

    def update_status(self):
        if self.status == 'OFF':
            return 'ON'
        elif self.status == 'ON':
            return 'OFF'

    def start_engines(self):
        if self.status == "OFF" and self.tank.fuel > 0:
            self.status = "ON"
            self.start_time = time()

            processes = []

            for e in self.engines:
                process = multiprocessing.Process(target=e.warm_up)
                processes.append(process)
                process.start()

            for p in processes:
                p.join()

    def get_ambient_pressure(self, altitude: int) -> float:
        """
        Calcule la pression atmosphérique en fonction de l'altitude en utilisant l'équation de l'atmosphère standard.
        Args:
            altitude (float): L'altitude en mètres.
        Return:
            float: La pression atmosphérique en Pascals (Pa).
        """
        P0 = 101325  # Pression au niveau de la mer en Pa
        L = 0.0065  # Gradient de température standard en K/m
        T0 = 288.15  # Température standard au niveau de la mer en K
        g = 9.81  # Accélération due à la gravité en m/s²
        M = 0.02896  # Masse molaire de l'air en kg/mol
        R = 8.314  # Constante spécifique des gaz pour l'air sec en J/(mol·K)

        return P0 * (1 - (L * altitude) / T0) ** ((g * M) / (R * L))

    # calcul
    def get_thrust(self):
        """
        Args :
            Débit massique : Il s'agit de la quantité de masse de gaz expulsée par unité de temps, mesurée en kilogrammes par seconde (kg/s).
            vitesse d'éjection des gaz : représente la vitesse à laquelle les gaz sont expulsés par le moteur ou le système de propulsion,
            généralement mesurée en mètres par seconde (m/s)
            Pression à l'échappement : C'est la pression des gaz à la sortie du moteur, généralement exprimée en pascals (Pa).
            Pression ambiante : Il s'agit de la pression de l'air environnant, également exprimée en pascals (Pa).
            Surface de sortie des gaz : C'est la surface à travers laquelle les gaz s'échappent, mesurée en mètres carrés (m²).
        :return:
            Force de poussée = Débit massique x Vitesse d'éjection des gaz + (Pression à l'échappement - Pression ambiante) x Surface de sortie des gaz
        """

        thrust_list = []
        for e in self.engines:
            mass_flow_rate = e.get_mass_flow_rate()
            exhaust_velocity = e.get_exhaust_velocity()  # vitesse d'éjection des gaz
            exhaust_pressure = e.get_exhaust_pressure()
            ambient_pressure = self.get_ambient_pressure()
            exit_area = e.get_exit_area()

            engine_thrust = mass_flow_rate * exhaust_velocity + (ambient_pressure - exhaust_pressure) * exit_area
            thrust_list.append(engine_thrust)

        return sum(thrust_list)

    def run(self):
        pass
