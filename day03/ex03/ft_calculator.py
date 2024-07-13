# I changed 'object' to 'operand' because 'object' is also a Python keyword
class Calculator():
    """Calculator class"""
    def __init__(self, values: list):
        """Constuctor of the Calculator class.

        Args:
            values (list): the values to create the internal array/
        """
        self.array = values

    def __add__(self, operand) -> None:
        """Adds operand to all the values in the array"""
        self.array = [i + operand for i in self.array]
        print(self.array)

    def __mul__(self, operand) -> None:
        """Multiplies all the values in the array by operand"""
        self.array = [i * operand for i in self.array]
        print(self.array)

    def __sub__(self, operand) -> None:
        """Substracts operand to all the values in the array"""
        self.array = [i - operand for i in self.array]
        print(self.array)

    def __truediv__(self, operand) -> None:
        """Divides all the values in the array by operand. Raises a
        ZeroDivisionError if operand is 0."""
        if operand == 0:
            raise ZeroDivisionError("Cannot divise by 0!")
        self.array = [i / operand for i in self.array]
        print(self.array)


def main():
    """Main function. Run subject's tests"""
    v1 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = Calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    try:
        v3 / 0
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
