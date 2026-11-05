def input_temperature(temp_str):
    return (int(temp_str))


def test_temperature():
    try:
        print("\nInput data is '25'")
        print(f"Temperature is now {input_temperature("25")}°C")
        print("\nInput data is 'abc'")
        input_temperature("abc")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    print("\nAll tests completed - program didn't crash!")


def main():
    print("=== Garden Temperature ===")
    test_temperature()


if __name__ == "__main__":
    main()
