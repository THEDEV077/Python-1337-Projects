class PlantNameError(Exception):
    pass


class GardenError(Exception):
    pass


class WaterError(GardenError):
    pass


class SunlightError(GardenError):
    pass


class PlantWaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name: str = name
        self.water: int = water
        self.sun: int = sun


class GardenManager:
    def __init__(self):
        self.plants: list[Plant] = []
        self.water_qnt: int = 15

    def add_plant(self, plants_list: list) -> None:
        for plant in plants_list:
            try:
                if not plant[0]:
                    raise PlantNameError(
                        "Error adding plant: Plant name cannot be empty!")
                self.plants += [Plant(plant[0], plant[1], plant[2])]
                print(f"Added {plant[0]} successfully")
            except PlantNameError as e:
                print(e)

    def water_plants(self) -> None:
        try:
            if (self.water_qnt <= 0):
                raise WaterError("Not enough water in the tank")
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
            print("System recovered and continuing...")
        finally:
            if self.water_qnt > 0:
                print("Closing watering system (cleanup)")

    def check_plant(self) -> None:
        for plant in self.plants:
            try:
                if not plant.name:
                    raise PlantNameError("Error: Plant name cannot be empty")
                if plant.water > 10:
                    raise PlantWaterError(
                        f"{plant.water} is too high (max 10)")
                if plant.water < 1:
                    raise PlantWaterError(
                        f"{plant.water} is too low (min 1)")
                if plant.sun < 2:
                    raise SunlightError(
                        f"{plant.sun} is too low (min 2)")
                if plant.sun > 12:
                    raise SunlightError(
                        f"{plant.sun} is too high (max 12)")
            except PlantWaterError as e:
                print(f"Error checking {plant.name}: Water level {e}")
            except SunlightError as e:
                print(f"Error checking {plant.name}: Sunlight hours {e}")
            except Exception as e:
                print(e)
            else:
                print(
                    f"{plant.name}: healthy (water: {plant.water},",
                    f"sun: {plant.sun})"
                )


def test_garden_management() -> None:
    M1: GardenManager = GardenManager()
    print("Adding plants to garden...")
    plants: list = [
        ["tomato", 5, 8],
        ["lettuce", 15, 12],
        ["", 10, 12]
    ]
    M1.add_plant(plants)
    print("\nWatering plants...")
    M1.water_plants()
    print("\nChecking plant health...")
    M1.check_plant()
    M1.water_qnt = 0
    print("\nTesting error recovery...")
    M1.water_plants()
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    try:
        print("=== Garden Management System ===\n")
        test_garden_management()
    except Exception as e:
        print(f"Caught an error: {e}")
