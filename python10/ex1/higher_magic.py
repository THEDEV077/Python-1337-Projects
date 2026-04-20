from collections.abc import Callable
from typing import List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> List[str]:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    print("\nTesting spell combiner...")

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    combined = spell_combiner(fireball, heal)
    result1 = combined("Dragon", 50)

    print(f"Combined spell result: {result1[0]}, {result1[1]}")

    print("\nTesting power amplifier...")

    def base_spell(target: str, power: int) -> str:
        return f"{power}"

    amplified = power_amplifier(base_spell, 3)

    original = 10
    result2 = amplified("Dragon", original)

    print(f"Original: {original}, Amplified: {result2}")
