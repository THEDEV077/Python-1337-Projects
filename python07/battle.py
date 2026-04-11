from ex0 import FlameFactory, AquaFactory
from ex0.creature import CreatureFactory, Creature


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(c1: Creature, c2: Creature) -> None:
    print("Testing battle")
    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())


flame_factory = FlameFactory()
aqua_factory = AquaFactory()
test_factory(flame_factory)
print()
test_factory(aqua_factory)
print()
test_battle(flame_factory.create_base(), aqua_factory.create_base())
