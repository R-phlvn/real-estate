from user import User
from region import Region
from random import choice
from estate import Apartment
from Advertisement import ApartmentSell

FIRST_NAME = ["Ali", "Reza", "Mehdi"]
LAST_NAME = ["Pahlavan", "Rahmani", "Razavi"]
PHONE_NUMBER = ['09354566565', '09931232354', '09154563443', '09388798720']

if __name__ == "__main__":
    for mobile in PHONE_NUMBER:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    reg1 = Region("Faramarz")
    Apt1 = Apartment(
        has_elevator=True, has_parking=True, floor=2,
        user=User.object_list[0], area=3, room_count=4,
        built_year=1400, region=reg1, address="Faramarz 1..."
    )
    Apt1.show_description()

    #Advertisement Object
    aps1 = ApartmentSell(
        has_elevator=True, has_parking=True, floor=2,
        user=User.object_list[0], area=3, room_count=4,
        built_year=1400, region=reg1, address="Faramarz 1...",
        price_per_meter=50, discountable=True, convertable=True

    )
    aps1.show_detail()