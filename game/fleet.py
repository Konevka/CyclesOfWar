class Fleet:
    def __init__(self, owner, target, forces):
        self._owner = owner
        self._target = target
        self._forces = forces

    @property
    def owner(self):
        return self._owner

    @property
    def target(self):
        return self._target

    @property
    def forces(self):
        return self._forces
