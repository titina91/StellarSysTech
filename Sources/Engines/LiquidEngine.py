from Sources.Engines.Engine import Engine


class LiquidEngine(Engine):

    default_mass_flow_rate = 100.0

    def __init__(self, label, specific_impulse, temperature, is_on_flag,_mass_flow_rate, propellant):
        super().__init__(label, specific_impulse, temperature, is_on_flag)
        self.propellant = propellant  # type de propergol liquide

        # own variable
        self._mass_flow_rate = LiquidEngine.default_mass_flow_rate

    def get_mass_flow_rate(self) -> float:
        return 100.0

