def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    power = list(map(lambda x: x["power"], mages))
    return {
        "max_power": max(power),
        "min_power": min(power),
        "avg_power": round(sum(power) / len(power), 2)
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85},
        {"name": "Fire Staff", "power": 92}
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)

    for i in range(len(sorted_artifacts) - 1):
        a1 = sorted_artifacts[i]
        a2 = sorted_artifacts[i + 1]
        print(f"{a1['name']} ({a1['power']} power) comes before {
            a2['name']} ({a2['power']} power)")

    print("Testing spell transformer...")
    transformed_spells = spell_transformer(spells)

    print(" ".join(transformed_spells))
