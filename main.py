from user import User
from region import Region
from random import choice
from estate import Apartment
from advertisement import ApartmentSell, ApartmentRent, HouseSell, HouseRent,\
    StoreSell, StoreRent

FIRST_NAME = ["Ali", "Reza", "Mehdi"]
LAST_NAME = ["Pahlavan", "Rahmani", "Razavi"]
PHONE_NUMBER = ['09354566565', '09931232354', '09154563443', '09388798720']

if __name__ == "__main__":
    for mobile in PHONE_NUMBER:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    faramarz = Region("Faramarz")
    vakilabad = Region("VakilAbad")
    
    #Advertisement Object
    aps1 = ApartmentSell(
        has_elevator=True, has_parking=True, floor=2,
        user=User.object_list[0], area=3, room_count=4,
        built_year=1400, region=faramarz, address="Faramarz 1...",
        price_per_meter=50, discountable=True, convertable=True
    )

    Hs1 = HouseSell(
        has_yard=True, floor_count=2,
        user=User.object_list[2], area=90, room_count=3,
        built_year=1400, region=vakilabad, address="VakilAbad 22...",
        price_per_meter=100, discountable=True, convertable=True
    )
    #Hs1.show_detail()

    Hs2 = HouseSell(
        has_yard=True, floor_count=2,
        user=User.object_list[2], area=90, room_count=3,
        built_year=1400, region=faramarz, address="Faramarz 22...",
        price_per_meter=100, discountable=True, convertable=True
    )

    res = HouseSell.manager.search(region=faramarz)
    print(res)