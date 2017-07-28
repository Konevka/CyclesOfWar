import numpy as np

import planet

class Universe:
    def __init__(self, seed, players, planets_per_player, width, height):
        self._fleets = []
        self._planets = []

        for player in players:
            self.create_start_planets(players, width, height)

    @property
    def fleets(self):
        return self._fleets

    @property
    def planets(self):
        return self._planets

    def create_start_planets(self, players, height, width):
        n = float(len(players))
        height_radius = height / 2.0
        width_radius = width / 2.0
        polygon_base = np.arange(n) / n * np.pi * 2.0
        x = np.cos(polygon_base) * width_radius + width_radius
        y = np.sin(polygon_base) * height_radius + height_radius

        for i, player in enumerate(players):
            self.planets.append(planet.Planet(x[i], y[i], player))

    def update(self, milliseconds):
        for planet in self.planets:
            planet.update(milliseconds)

        for fleet in self.fleets:
            fleet.update(milliseconds)
            if fleet.arrived():
                fleet.target.land(fleet)
