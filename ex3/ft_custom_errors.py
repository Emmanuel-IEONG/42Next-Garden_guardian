class GardenError(Exception):
    def __init__(self, message):
        super().__init__(f"{message}")


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(f"{message}")


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(f"{message}")


def temperature_too_hot():
    temperature = 50
    if (temperature > 40):
        raise PlantError("The tomato plant is wilting!")


def not_enough_water():
    water_volume = 10
    if (water_volume < 20):
        raise WaterError("Not enough water in the tank!")


def test_plant():
    print("\nTesting PlantError...")
    try:
        temperature_too_hot()
    except PlantError as err:
        print(f"Caught PlantError: {err}")


def test_water():
    print("\nTesting WaterError...")
    try:
        not_enough_water()
    except WaterError as err:
        print(f"Caught WaterError: {err}")


def test_all_errors():
    print("\nTesting catching all garden errors...")
    try:
        temperature_too_hot()
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    try:
        not_enough_water()
    except GardenError as err:
        print(f"Caught GardenError: {err}")


def main():
    print("=== Custom Garden Errors Demo ===")
    test_plant()
    test_water()
    test_all_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
