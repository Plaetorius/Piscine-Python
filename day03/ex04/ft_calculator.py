class Calculator():
    """Calculator Class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Prints the dot product of the two vectors

        Args:
            V1 (list[float]): vector 1
            V2 (list[float]): vector 2
        """
        print("Dot product is: "
              + str(sum([float(i) * float(j) for i, j in zip(V1, V2)])))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Prints the addition of two vectors

        Args:
            V1 (list[float]): vector 1
            V2 (list[float]): vector 2
        """
        print("Add Vector is: "
              + str([float(i) + float(j) for i, j in zip(V1, V2)]))

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Prints the soustraction of two vectors

        Args:
            V1 (list[float]): vector 1
            V2 (list[float]): vector 2
        """
        print("Sous Vector is: "
              + str([float(i) - float(j) for i, j in zip(V1, V2)]))


def main():
    """Main function. Run subject's tests"""
    a = [5.0, 10.0, 2.0]
    b = [2.0, 4.0, 3.0]
    Calculator.dotproduct(a, b)
    Calculator.add_vec(a, b)
    Calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
