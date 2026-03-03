class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days")


class Flower(Plant):
    species: str = "Flower"

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name.capitalize()} is blooming beautifully!")

    def get_info(self) -> None:
        print(
            f"{self.name.capitalize()} (Flower):",
            f"{self.height}cm, {self.age} days, {self.color} color"
        )


class Tree(Plant):
    species: str = "Tree"

    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        x = 3.14 * (self.trunk_diameter / 2) ** 2 * 0.04
        print(
            f"{self.name.capitalize()}",
            f"provides {x:.0f} square meters of shade"
        )

    def get_info(self) -> None:
        print(
            f"{self.name} (Tree): {self.height}cm,",
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    species: str = "Vegetable"

    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: float
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm,",
              f"{self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin C")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    plants: list[Plant] = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 30, 20, "yellow"),
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 600, 2000, 40),
        Vegetable("Tomato", 80, 90, "summer", 9.5),
        Vegetable("Carrot", 25, 70, "spring", 8.0),
    ]
    for plant in plants:
        print("")
        plant.get_info()
        if plant.species == "Flower":
            plant.bloom()
        elif plant.species == "Tree":
            plant.produce_shade()
