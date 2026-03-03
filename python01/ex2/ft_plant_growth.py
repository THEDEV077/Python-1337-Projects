class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, height: int) -> None:
        self.height += height

    def grow_older(self, age: int) -> None:
        self.age += age

    def get_info(self) -> None:
        print(
            f"{self.name.capitalize()}:",
            f"{self.height}cm, {self.age} days old"
        )


if __name__ == "__main__":
    p: Plant = Plant("Rose", 25, 30)
    for i in range(7):
        if i in (0, 6):
            print(f"=== Day {i + 1} ===")
            p.get_info()
        p.grow(1)
        p.grow_older(1)
    print(f"Growth this week: +{i}cm")
