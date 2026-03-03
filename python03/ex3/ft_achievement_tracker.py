if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    achievements: dict = {
        "alice": {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'},
        "bob": {'first_kill', 'level_10', 'boss_slayer', 'collector'},
        "charlie": {
            'level_10',
            'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
    }
    all_achivement: set = set()
    all_intersection: set = achievements["alice"]
    rare_achivement: set = set()
    for player in achievements:
        print(f"Player {player} achievements: {achievements[player]}")
        all_achivement = achievements[player].union(all_achivement)
        all_intersection = achievements[player].intersection(all_intersection)
        achievements_union: set = set()
        for player1 in achievements:
            if player != player1:
                achievements_union = achievements[player1].union(
                    achievements_union)
        rare_achivement = rare_achivement.union(
            achievements[player].difference(achievements_union))

    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {all_achivement}")
    print(f"Total unique achievements: {len(all_achivement)}")
    print(f"\nCommon to all players: {all_intersection}")
    print(f"Rare achievements (1 player): {rare_achivement}\n")
    print("Alice vs Bob common:",
          achievements["alice"].intersection(achievements["bob"]))
    print(f"Alice unique: {achievements["alice"] - achievements["bob"]}")
    print(f"Bob unique: {achievements["bob"] - achievements["alice"]}")
