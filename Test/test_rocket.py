import time
import unittest

from Rocket import Rocket
from Sources.Engines.Engine import Engine
from Stage import Stage


class RocketTest(unittest.TestCase):

    def setUp(self):
        self.rocket = Rocket()

        # create Stages
        self.rocket.firstStage = Stage(label="First stage",
                                       status="OFF",
                                       empty_weight=1000,
                                       burn_time=300,
                                       max_thrust=1000
                                       )

        self.rocket.secondStage = Stage(label="Second stage",
                                        status="OFF",
                                        empty_weight=1000,
                                        burn_time=300,
                                        max_thrust=1000
                                        )

        self.rocket.thirdStage = Stage(label="Third stage",
                                       status="OFF",
                                       empty_weight=1000,
                                       burn_time=300,
                                       max_thrust=1000
                                       )

        # create engines
        self.rocket.firstStage.engines = {Engine() for i in range(5)}
        self.rocket.secondStage.engines = {Engine() for i in range(5)}
        self.rocket.thirdStage.engines = {Engine() for i in range(5)}

        # add stages to the rocket
        self.rocket.add_stage(self.rocket.firstStage)
        self.rocket.add_stage(self.rocket.secondStage)
        self.rocket.add_stage(self.rocket.thirdStage)

    def test_calcul_mass(self):
        mass = self.rocket.calcul_mass()
        expected_mass = 18000
        self.assertEqual(mass, expected_mass, "mass should be 12000")  # add assertion here

    def test_start_discount(self):
        start_time = time.time()
        self.rocket.start_discount()
        end_time = time.time()
        self.assertTrue(9 < end_time - start_time < 11, "the countdown should have lasted 10s")


if __name__ == '__main__':
    unittest.main()
