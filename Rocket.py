import multiprocessing

from Stage import Stage
from time import sleep, gmtime, strftime
from Decorators.Time_Decorators import measure_execution_time


def _check_condition(condition, confirmation_message):
    while True:
        answer = input(condition).lower()
        if answer in ["y", 'yes']:
            print(confirmation_message[0])
            return True
        elif answer in ["n", "no"]:
            print(confirmation_message[1])
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def _check_weather_condition() -> bool:
    """
    La fonction vérifie si les conditions météorologiques actuel sont conforme à un décollage en toute sécurité
    :param self:
    :return: renvoie un booleen
    """
    return _check_condition("Are the weather conditions favorable?(y/n)",
                            ["Weather condition are optimal",
                             "Weather condition are not optimal yet"])


def _check_propulsion_system() -> bool:
    """
    La fonction vérifie si le système de propulsion est opérationnel à un décollage en toute sécurité
    :return: renvoie un booleen
    """
    return _check_condition("Is the propulsion system operational?(y/n)",
                            ["propulsion system is operational",
                             "propulsion system is not operational yet"])


def _check_communication_system() -> bool:
    """
    La fonction vérifie si le système de communication avec la tour de contrôle est opérationnel à un décollage en toute sécurité
    :return: renvoie un booleen
    """
    return _check_condition("Is the communication system operational?(y/n)",
                            ["communication system is operational",
                             "communication system is not operational yet"])


class Rocket:
    # id increment
    id = 0

    def __init__(self):
        # automatically increment id
        Rocket.id += 1

        self.id = Rocket.id
        self.altitude = 0
        self.velocity = 0
        self.mass = 0
        self.stages = []
        self.engines_ready = False

    def add_stage(self, stage: Stage) -> None:
        self.stages.append(stage)
        print(stage)

    # calcul
    def calcul_mass(self):
        answer = sum([stage.mass for stage in self.stages])
        print(answer)
        return answer

    def calculate_speed(self):
        pass

    def calculate_acceleration(self):
        pass

    def calculate_thrust(self):
        self.stages[0].calculate_thrust()

    # rocket state
    @measure_execution_time
    def start_discount(self):
        for i in range(10, 0, -1):
            sleep(1)
            #print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
            print(i)
        print("FEU !!!")
        return 1

    @measure_execution_time
    def start_engines(self):
        """
        Demarre les etages
        :return:
        """
        print("START WARMING")
        sleep(3)
        processes = []

        # initialize all stages in parallel
        for stage in self.stages:
            print(f"Stage : {stage.id} -- {stage.label}")
            process = multiprocessing.Process(target=stage.start_engines)
            processes.append(process)
            process.start()

        for p in processes:
            p.join()

        return 1

    def pre_launch_phase(self):
        if _check_weather_condition() and _check_propulsion_system() and _check_communication_system():
            while True:
                answer = input("Are we allowed to take off(y/n)").lower()
                if answer in ["y", 'yes']:
                    print("START LAUNCH")
                    break
                elif answer in ["n", "no"]:
                    print("Please wait")
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        self.start_discount()

    def start_rocket(self):
        while True:
            answer = input("Do you want to start rocket? (y/n)").lower()
            if answer in ["y", 'yes']:
                self.engines_ready = not self.engines_ready
                break
            elif answer in ["n", "no"]:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        self.start_engines()
        self.pre_launch_phase()

    def unhook_stage(self):
        removed_stage = self.stages.pop(0) if len(self.stages) > 1 else None
        if removed_stage is None:
            print("There is no stage!")
