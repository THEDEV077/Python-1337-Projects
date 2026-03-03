def water_plants(plant_list: list) -> bool:
    if plant_list.__class__.__name__ != "list":
        raise TypeError("error: wrong type (must be a list)")
    print("Opening watering system")
    success: bool = False
    try:
        for plant in plant_list:
            if not plant:
                raise Exception("Error: Cannot water None - invalid plant!")
            print(f"Watering {plant}")
        success = True
    except Exception as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
    return success


def test_watering_system() -> None:
    try:
        print("Testing normal watering...")
        plant_list1: list = ["tomato", "lettuce", "carrots"]
        if water_plants(plant_list1):
            print("Watering completed successfully!\n")
        print("Testing with error...")
        plant_list2: list = ["tomato", "", "lettuce", "carrots"]
        if water_plants(plant_list2):
            print("Watering completed successfully!\n")
    except Exception as e:
        print(e)
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
