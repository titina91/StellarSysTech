from Engine import Engine


class LiquidEngine(Engine):
    def __init__(self, propellant):
        super().__init__("label", "isp", "temperature", "is_on_flag")
        self.propellant = propellant    # type de propergol liquide
