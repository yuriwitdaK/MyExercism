class SpaceAge:
    EARTH_YEAR = 31557600

    PLANET_FACTORS = {
        "Earth": 1.0,
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132
    }

    def __init__(self, seconds):
        self.seconds = seconds

    # Generische Methode
    def on_planet(self, planet):
        factor = self.PLANET_FACTORS[planet]
        return self.seconds / (self.EARTH_YEAR * factor)

# Dynamische Methoden außerhalb der Klasse erzeugen
for planet, factor in SpaceAge.PLANET_FACTORS.items():
    def make_method(f):
        return lambda self: round(self.seconds / (SpaceAge.EARTH_YEAR * f), 2)
    setattr(SpaceAge, f'on_{planet.lower()}', make_method(factor))