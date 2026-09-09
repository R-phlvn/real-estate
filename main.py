from sample import create_sample
from advertisement import ApartmentSell, ApartmentRent, HouseSell, HouseRent,\
    StoreSell, StoreRent

class Handler:
    ADVERTISEMENT_TYPES = {
        1: ApartmentSell, 2: ApartmentRent,
        3: HouseSell, 4: HouseRent,
        5: StoreSell, 6: StoreRent
    }

    SWITCHES = {
        'r': "get reports",
        's': "show all"
    }

    def get_reports(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            print(adv)
            if adv.manager is not None:
                print(adv, adv.manager.count())
            else:
                print(adv, "No manager defined")

    def show_all(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            for obj in adv.object_list:
                print(obj.show_detail())

    def run(self):
        for key in self.SWITCHES:
            print(f"press {key} for {self.SWITCHES[key]}")

        user_input = input("Enter your choice: ")
        switch = self.SWITCHES.get(user_input, None) 
        if switch is None:
            print("Invalid input")
            self.run()

        choice = getattr(self, switch, None)
        choice()
        self.run()
    


if __name__ == "__main__":
    create_sample()
    handler = Handler().run()