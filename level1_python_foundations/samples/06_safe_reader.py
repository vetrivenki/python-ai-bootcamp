# 06_safe_reader.py
# Level 1 — Topic 6: Error handling and custom exceptions

class FileEmptyError(Exception):
    """Raised when a file is empty."""
    pass


class InvalidFormatError(Exception):
    """Raised when file content is not in expected format."""
    pass


def safe_read_numbers(filepath: str) -> list[float]:
    try:
        with open(filepath, "r") as f:
            content = f.read().strip()

        if not content:
            raise FileEmptyError(f"File '{filepath}' is empty")

        numbers = []
        for line in content.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                numbers.append(float(line))
            except ValueError:
                raise InvalidFormatError(f"Invalid number found: '{line}'")

        return numbers

    except FileNotFoundError:
        print(f"Error: File '{filepath}' does not exist.")
        return []
    except FileEmptyError as e:
        print(f"Custom Error: {e}")
        return []
    except InvalidFormatError as e:
        print(f"Custom Error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


if __name__ == "__main__":
    # Create a test file
    with open("numbers.txt", "w") as f:
        f.write("10\n20\n3.5\nabc\n40\n")

    print(safe_read_numbers("numbers.txt"))
    print(safe_read_numbers("nonexistent.txt"))
