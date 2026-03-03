class GardenManager:
    gardens: list["GardenManager"] = []
    total: int = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.plants: list[GardenManager.Plant] = []
        self.total_growth = 0
        GardenManager.gardens.append(self)
        GardenManager.total += 1

    def count_plants(x: int, y: int, z: int) -> None:
        print((f"Plant types: {z} regular, {y} flowering, {x} prize flowers"))

    count_plants = staticmethod(count_plants)

    def get_score(self) -> int:
        score: int = 0
        for plant in self.plants:
            if plant.height > 10:
                score += 10
            if plant.species == "PrizeFlower":
                score += 10
        return score

    def garden_stats(self):
        x, y, z = 0, 0, 0
        print(f"\n=== {self.name.capitalize()}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if plant.species == "PrizeFlower":
                print(
                    f"- {plant.name.capitalize()}:",
                    f"{plant.height}cm, {plant.color}",
                    f"flowers (blooming), Prize points: {plant.prize}"
                )
                x += 1
            elif plant.species == "FloweringPlant":
                print(
                    f"- {plant.name}: {plant.height}cm,",
                    f"{plant.color} flowers (blooming)"
                )
                y += 1
            else:
                print(f"- {plant.name}: {plant.height}cm")
                z += 1
        print(
            "\nPlants added:",
            f"{x + y + z}, Total growth: {self.total_growth}cm"
        )
        GardenManager.count_plants(x, y, z)

    def create_garden_network(cls) -> list["GardenManager"]:
        alice: GardenManager = cls("alice")
        bob: GardenManager = cls("bob")
        return [alice, bob]

    create_garden_network = classmethod(create_garden_network)

    def add_plant(self, plant: "Plant") -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name.capitalize()}'s garden")

    def help_plants(self, height: int) -> None:
        print(f"\n{self.name.capitalize()} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(height)
            self.total_growth += height

    def print_total() -> None:
        totalGardien: int = 0
        for garden in GardenManager.gardens:
            totalGardien += 1
        print(f"Total gardens managed: {totalGardien}")

    print_total = staticmethod(print_total)

    def validate_height(height: int) -> None:
        print(f"Height validation test: {str(height > 0)}")

    validate_height = staticmethod(validate_height)

    class Plant:
        species: str = "Plant"

        def __init__(self, name: str, height: int, age: int) -> None:
            self.name = name
            self.height = height
            self.age = age

        def grow(self, height: int) -> None:
            self.height += height
            print(f"{self.name.capitalize()} grew {height}cm")

    class FloweringPlant(Plant):
        species: str = "FloweringPlant"

        def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str
        ) -> None:
            super().__init__(name, height, age)
            self.color = color

    class PrizeFlower(FloweringPlant):
        species: str = "PrizeFlower"

        def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str,
            prize: int
        ) -> None:
            super().__init__(name, height, age, color)
            self.prize = prize


def print_score() -> None:
    print("Garden scores - ", end="")
    for garden in GardenManager.gardens[:-1]:
        print(f"{garden.name}: {garden.get_score()},", end="")
    if GardenManager.gardens:
        last = GardenManager.gardens[-1]
        print(f"{last.name}: {last.get_score()}")


if (__name__ == "__main__"):
    print("=== Garden Management System Demo ===\n")
    M1: GardenManager = GardenManager("alice")
    M2: GardenManager = GardenManager("Bob")
    plants: list[GardenManager.Plant] = [
        GardenManager.Plant("Oak Tree", 100, 30),
        GardenManager.FloweringPlant("Rose", 25, 15, "red"),
        GardenManager.PrizeFlower("Sunflower", 50, 17, "yellow", 10)
    ]
    for plant in plants:
        M1.add_plant(plant)
    M1.help_plants(1)
    M1.garden_stats()
    print("")
    GardenManager.validate_height(M1.plants[0].height)
    print_score()
    GardenManager.print_total()
