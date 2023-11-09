from Engine import Engine
from Rocket import Rocket
from time import sleep

# Press the green button in the gutter to run the script.
from Stage import Stage

if __name__ == '__main__':

    rocket = Rocket()

    # create Stages
    firstStage = Stage(label="First stage",
                       status="OFF",
                       empty_weight=1000,
                       burn_time=300,
                       max_thrust=1000
                       )

    secondStage = Stage(label="Second stage",
                        status="OFF",
                        empty_weight=1000,
                        burn_time=300,
                        max_thrust=1000
                        )

    thirdStage = Stage(label="Third stage",
                       status="OFF",
                       empty_weight=1000,
                       burn_time=300,
                       max_thrust=1000
                       )

    # create engines
    firstStage.engines = {Engine() for i in range(5)}
    secondStage.engines = {Engine() for i in range(5)}
    thirdStage.engines = {Engine() for i in range(5)}

    # add stages to the rocket
    rocket.add_stage(firstStage)
    rocket.add_stage(secondStage)
    rocket.add_stage(thirdStage)

    print("First Stage")
    for e in firstStage.engines: print(e)

    print("Second Stage")
    for e in secondStage.engines: print(e)

    print("Third Stage")
    for e in thirdStage.engines: print(e)
    rocket.start_rocket()

