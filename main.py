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
        'r': "get_reports",
        's': "show_all"
    }

    def get_reports(self):
        print("\n--- Reports ---")
        for adv in self.ADVERTISEMENT_TYPES.values():
            count = adv.manager.count() if adv.manager is not None else 0
            print(f"{adv.__name__}: {count} records")
        print("-" * 15 + "\n")

    def show_all(self):
        print("\n--- All Advertisements ---")
        for adv in self.ADVERTISEMENT_TYPES.values():
            if adv.object_list:
                print(f"*** {adv.__name__} ***")
                for obj in adv.object_list:
                    obj.show_detail()
                    print("-" * 20)
        print("\n")

    def run(self):
        while True:
            for key in self.SWITCHES:
                print(f"press {key} for {self.SWITCHES[key]}")
            print("press q to exit")

            user_input = input("Enter your choice: ")

            if user_input.lower() == 'q':
                print("Exiting...")
                break

            switch = self.SWITCHES.get(user_input, None) 

            if switch is None:
                print("Invalid input! Try again.\n")
                continue

            choice = getattr(self, switch, None)
            if choice:
                choice()
    


if __name__ == "__main__":
    create_sample()
    handler = Handler()
    handler.run()