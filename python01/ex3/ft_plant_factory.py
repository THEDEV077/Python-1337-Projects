class Plant:
    p: int = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.p += 1

    def grow(self, height: int) -> None:
        self.height += height

    def grow_older(self, age: int) -> None:
        self.age += age

    def get_info(self) -> None:
        print(
            f"Created: {self.name.capitalize()}",
            f"({self.height}cm, {self.age} days)"
        )


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    for plant in plants:
        plant.get_info()

    print(f"\nTotal plants created: {Plant.p}")
