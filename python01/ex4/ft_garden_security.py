class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        print(f"Plant created: {self.name.capitalize()}")
        if height < 0:
            print(f"\nInvalid operation attempted: height {height}cm"
                  + " [REJECTED]")
            print("Security: Negative height rejected\n")
            self.__height = 0
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        if age < 0:
            print(f"\nInvalid operation attempted: age {age}cm [REJECTED]")
            print("Security: Negative age rejected\n")
            self.__age = 0
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"\nInvalid operation attempted: height {height}cm"
                  + " [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"\nInvalid operation attempted: age {age}cm [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_info(self) -> None:
        print(f"Current plant: {self.name.capitalize()} ({self.__height}cm,",
              f"{self.__age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p: SecurePlant = SecurePlant("Rose", 25, 30)
    p.set_height(-5)
    p.get_info()
