class PlantError(Exception):
    def __init__(self, message):
        super().__init__(f"{message}")


def water_plant(plant_name):
    if (plant_name == plant_name.capitalize()):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: ’{plant_name}’")


def test_watering_system(tomato, lettuce, carrots):
    print("Opening watering system")
    try:
        water_plant(tomato)
        water_plant(lettuce)
        water_plant(carrots)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


def test_valid_plant():
    print("\nTesting valid plants...")
    test_watering_system("Tomato", "Lettuce", "Carrots")


def test_invalid_plant():
    print("\nTesting invalid plants...")
    test_watering_system("Tomato", "lettuce", "carrots")


def main():
    print("=== Garden Watering System ===")
    test_valid_plant()
    test_invalid_plant()
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
