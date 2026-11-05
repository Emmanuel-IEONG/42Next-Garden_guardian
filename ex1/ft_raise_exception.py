class TemperatureError(ValueError):
    def __init__(self, temperature):
        self.temperature = temperature
        if temperature < 0:
            err_msg = f"{temperature}°C is too cold for plants (min 0°C)"
        else:
            err_msg = f"{temperature}°C is too hot for plants (max 40°C)"
        super().__init__(err_msg)


def input_temperature(temp_str):
    temp_nb = int(temp_str)
    if (temp_nb >= 0 and temp_nb <= 40):
        return (temp_nb)
    else:
        raise TemperatureError(temp_nb)


def test_temperature():
    for temp_str in ["25", "abc", "100", "-50"]:
        print(f"\nInput data is '{temp_str}'")
        try:
            temperature = input_temperature(temp_str)
        except ValueError as err:
            print(f"Caught input_temperature error: {err}")
        else:
            print(f"Temperature is now {temperature}°C")

    print("\nAll tests completed - program didn't crash!")


def main():
    print("=== Garden Temperature Checker ===")
    test_temperature()


if __name__ == "__main__":
    main()
