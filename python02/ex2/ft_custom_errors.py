class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, name: str) -> None:
        super().__init__(f"The {name} plant is wilting!")


class WaterError(GardenError):
    pass


def testing_plant(name: str) -> None:
    try:
        print("Testing PlantError...")
        raise PlantError(name)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")


def testing_water(qnt: int) -> None:
    try:
        print("Testing WaterError...")
        if qnt <= 0:
            raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")


def testing_garden(name: str, qnt: int) -> None:
    print("Testing catching all garden errors...")
    try:
        raise PlantError(name)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        if qnt <= 0:
            raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    try:
        print("=== Custom Garden Errors Demo ===\n")
        name: str = "tomato"
        qnt: int = -5
        testing_plant(name)
        testing_water(qnt)
        testing_garden(name, qnt)
    except Exception as e:
        print(f"Caught an error: {e}")
