class Tank:
    # id increment
    nb_id = 0

    def __init__(self, fuel=10000, temperature=0, mass=1000):
        self.fuel = fuel
        self.temperature = temperature
        self.mass = mass

    def __str__(self):
        return f"Tank " \
               f"fuel = {self.fuel}" \
               f"temperature = {self.temperature}" \
               f"mass = {self.mass}"
