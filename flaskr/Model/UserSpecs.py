class UserSpecs:

    def __init__(self, rooms, toilets, m2):
        self._rooms = rooms
        self._toilets = toilets
        self._m2 = m2

    def get_rooms(self):
        return self._rooms

    def set_rooms(self, rooms):
        self._rooms = rooms

    def get_toilets(self):
        return self._toilets

    def set_toilets(self, toilets):
        self._toilets = toilets

    def get_m2(self):
        return self._m2

    def set_m2(self, m2):
        self._m2 = m2

    def __str__(self):
        return str(self._rooms) + ", " + str(self._toilets) + ", " + str(self._m2)
