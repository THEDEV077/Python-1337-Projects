import time
from functools import wraps
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        print(f"Casting {func.__name__}...")
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")

        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, spell_name, power) -> Callable:
            if power >= min_power:
                return func(self, spell_name, power)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Callable:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt {
                            attempt}/{max_attempts})")
                    else:
                        print(f"Spell casting failed after {
                            max_attempts} attempts")
                        print("Waaaaaaagh spelled !")
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("\nTesting spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def unstable_spell():
        raise Exception("fail")

    unstable_spell()

    print("\nTesting MageGuild...")

    guild = MageGuild()

    print(guild.validate_mage_name("Merlin"))
    print(guild.validate_mage_name("x"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fire", 5))
