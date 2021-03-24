class UserSpecs:

    def __init__(rooms, toilets, m2):
        self._rooms = rooms
        self._toilets = toilets
        self._m2 = m2
    
    def get_rooms():
        return self._rooms

    def set_rooms(rooms):
        self._rooms = rooms
    
    def get_toilets():
        return self._toilets

    def set_toilets(toilets):
        self._toilets = toilets
    
    def get_m2():
        return self._m2

    def set_m2(m2):
        self._m2 = m2
    
    def __str__():
        return str(self._rooms) +", " + str(self._toilets) +", "+ str(self._m2)
    
