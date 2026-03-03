class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def print_plant(self) -> None:
        print(
            f"{self.name.capitalize()}:",
            f"{self.height}cm, {self.age} days old"
        )


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    p1: Plant = Plant("Rose", 25, 30)
    p1.print_plant()
    p2: Plant = Plant("Sunflower", 80, 45)
    p2.print_plant()
    p3: Plant = Plant("Cactus", 15, 120)
    p3.print_plant()
