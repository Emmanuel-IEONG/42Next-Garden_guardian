def garden_operations(operation_number):
    print(f"Testing operation {operation_number}...")
    match operation_number:
        case 0:
            return (int('abc'))
        case 1:
            return (10 / 0)
        case 2:
            return (open('non/existent/file', 'r'))
        case 3:
            return ("test" + 3)
        case _:
            return (print("Operation completed successfully"))


def test_error_types():
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        try:
            garden_operations(i)
        except ValueError as err:
            print(f"Caught ValueError: {err}")
        except ZeroDivisionError as err:
            print(f"Caught ZeroDivisionError: {err}")
        except FileNotFoundError as err:
            print(f"Caught FileNotFoundError: {err}")
        except TypeError as err:
            print(f"Caught TypeError: {err}")

    print("\nAll error types tested successfully!")


def main():
    test_error_types()


if __name__ == "__main__":
    main()
