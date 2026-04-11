from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import FlameFactory, AquaFactory
from ex2 import (NormalStrategy,
                          DefensiveStrategy,
                          AggressiveStrategy,
                          InvalidStrategyError)


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            print("\n* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                strategy1.act(c1)
                strategy2.act(c2)

            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


print("Tournament 0 (basic)")
print("[ (Flameling+Normal), (Healing+Defensive) ]")

battle([
    (FlameFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy())
])

print("\nTournament 1 (error)")
print("[ (Flameling+Aggressive), (Healing+Defensive) ]")

battle([
    (FlameFactory(), AggressiveStrategy()),  # invalid
    (HealingCreatureFactory(), DefensiveStrategy())
])

print("\nTournament 2 (multiple)")
print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")

battle([
    (AquaFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
    (TransformCreatureFactory(), AggressiveStrategy())
])
