from Base import BaseClass
from abc import abstractmethod

class EstateAbstract(BaseClass):
    def __init__(self, user, area, room_count, built_year, region, address, *args, **kwargs):
        self.user = user
        self.area = area
        self.room_count = room_count
        self.built_year = built_year
        self.region = region
        self.address = address
        super().__init__(*args, **kwargs)

    @abstractmethod
    def show_description(self):
        pass

class Apartment(EstateAbstract):
    def __init__(self, has_elevator, has_parking, floor, *args, **kwargs):
        self.has_elevator = has_elevator
        self.has_parking = has_parking
        self.floor = floor
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f"Apartment {self._id}: elevator: {self.has_elevator}, "
              f"parking: {self.has_parking}, floor: {self.floor}")
        
class House(EstateAbstract):
    def __init__(self, has_yard, floor_count, *args, **kwargs):
        self.has_yard = has_yard
        self.floor_count = floor_count
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f"Apartment {self._id}"
              f" yard: {self.has_yard}, floor: {self.floor_count}")
        
class Store(EstateAbstract):
    def show_description(self):
        pass