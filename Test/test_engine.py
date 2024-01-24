import unittest

import time
from Sources.Engines.Engine import Engine
from Tank import Tank

TEMPERATURE_MAX = 800  # température max
TEMPERATURE_MIN = 100  # température min


class EngineTest(unittest.TestCase):

    def setUp(self):
        self.engine = Engine(label="Test engine",
                             isp=250,
                             temperature=20,
                             is_on_flag=False,
                             associated_tank=Tank(fuel=10)
                             )
    def wait_for_thread_completion(self, thread):
        thread.join(timeout=5)
        self.assertFalse(thread.is_alive(), f"{thread.name} is still alive after completion.")

    def test_start_and_shutdown(self):
        # Verifie si le moteur est initialement eteint
        self.assertFalse(self.engine.is_on_flag)

        # verifie si le moteur est allumé après l'appel de start_engine
        self.engine.start_engine()
        self.assertTrue(self.engine.is_on_flag)

        # vérifie que les thread se lancent
        self.wait_for_thread_completion(self.engine.burnThread.join())
        self.wait_for_thread_completion(self.engine.temperatureThread.join())

        # eteindre le moteur
        self.engine.shutdown_engine()
        self.assertFalse(self.engine.is_on_flag)

        # assurer que les thread s'eteignent
        self.wait_for_thread_completion(self.engine.burnThread.join())
        self.wait_for_thread_completion(self.engine.temperatureThread.join())

    def test_control_temperature(self):

        # Verifie si le moteur est initialement eteint
        self.assertFalse(self.engine.is_on_flag)

        # allumer le moteur
        self.engine.is_on_flag = True
        self.assertTrue(self.engine.is_on_flag)
        self.assertTrue(self.engine.is_on_flag)

        # vérifier que la temperature minimum n'est pas encore atteinte
        self.assertTrue(self.engine.temperature < TEMPERATURE_MIN)

        # lancer le thread pour le control de la temperature
        self.engine.temperatureThread.start()

        # le moteur atteint la temperature minimum et se régule
        self.engine.temperature = TEMPERATURE_MIN
        print(f"temperature : {self.engine.temperature}")
        start_time = time.time()
        while time.time() - start_time < 10:
            if TEMPERATURE_MIN - 4 <= self.engine.temperature <= TEMPERATURE_MIN - 1:
                break
        self.assertTrue(TEMPERATURE_MIN - 4 <= self.engine.temperature <= TEMPERATURE_MIN - 1)

        # le moteur atteint la temperature maximum
        self.engine.temperature = TEMPERATURE_MAX
        print(f"temperature : {self.engine.temperature}")
        start_time = time.time()
        while time.time() - start_time < 20:
            if TEMPERATURE_MAX - 4 <= self.engine.temperature <= TEMPERATURE_MAX - 1:
                break
        self.assertTrue(TEMPERATURE_MAX - 4 <= self.engine.temperature <= TEMPERATURE_MAX - 1)

    def test_has_enough_fuel(self):
        # verifier s'il y a assez de carburant il renvoit la bonne réponse
        self.engine.consumption = 5
        self.assertTrue(self.engine.has_enough_fuel())

        # verifier s'il y a juste assez de carburant il renvoit la bonne réponse
        self.engine.consumption = 10
        self.assertTrue(self.engine.has_enough_fuel())

        # verifier s'il n'y a pas assez de carburant il renvoit la bonne réponse
        self.engine.consumption = 15
        self.assertFalse(self.engine.has_enough_fuel())


if __name__ == '__main__':
    unittest.main()
