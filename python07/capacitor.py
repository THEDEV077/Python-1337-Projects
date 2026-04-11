from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0.creature import Creature
from ex1.heal import HealCapability
from ex1.transform import TransformCapability
# from typing import Any


def test_heal(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, HealCapability):
        print(creature.heal())


def test_transform(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


factory = HealingCreatureFactory()
print("Testing Creature with healing capability")

heal_base = factory.create_base()
heal_evolved = factory.create_evolved()
print("base:")
test_heal(heal_base)
print("evolved:")
test_heal(heal_evolved)


factory1 = TransformCreatureFactory()
print("\nTesting Creature with transform capability")

transform_base = factory1.create_base()
transform_evolved = factory1.create_evolved()
print("base:")
test_transform(transform_base)
print("evolved:")
test_transform(transform_evolved)
