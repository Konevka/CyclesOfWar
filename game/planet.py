class Planet:
    INITIAL_FLEET_MODIFIER = 10

    def __init__(self):
        self._forces = 0
        self._production_rate = 0
        self._owner = None

    @property
    def forces(self):
        return self._forces

    @forces.setter
    def forces(self, value):
        self._forces = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner

    def land(self, fleet):
        if fleet.owner == self.owner:
            self.forces += fleet.forces
        elif fleet.forces <= self.forces:
            self.forces -= fleet.forces
        else:
            self.owner = fleet.owner
            self.forces = fleet.forces - self.forces