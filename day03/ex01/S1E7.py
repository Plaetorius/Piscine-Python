from S1E9 import Character


class Baratheon(Character):
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor of the Baratheon class. Does checks on whether the given
        arguments are of correct type. If not, raises a TypeError and sets
        default values.

        Args:
            first_name (str): The name of the Character
            is_alive (bool, optional): The life status of the Character.
                Defaults to True.
        """
        if isinstance(first_name, str):
            self.first_name = first_name
        else:
            print("first_name must be a string. Setting it to 'default'")
            self.first_name = 'default'
        if isinstance(is_alive, bool):
            self.is_alive = is_alive
        else:
            print("is_alive must be bool. Setting it to True")
            self.is_alive = True

    def __str__(self):
        return f""

    def __repr__(self):
        return f""

    @classmethod
    def create_baratheon():
        pass


class Lannister(Character):
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor of the Character class. Does checks on whether the given
        arguments are of correct type. If not, raises a TypeError and sets
        default values.

        Args:
            first_name (str): The name of the Character
            is_alive (bool, optional): The life status of the Character.
                Defaults to True.

        Raises:
            TypeError: raised if first_name isn't a string. Sets first_name
                to 'default'
            TypeError: raised if is_alive isn't a bool. Sets is_alive to True.
        """
        if isinstance(first_name, str):
            self.first_name = first_name
        else:
            print("first_name must be a string. Setting it to 'default'")
            self.first_name = 'default'
        if isinstance(is_alive, bool):
            self.is_alive = is_alive
        else:
            print("is_alive must be bool. Setting it to True")
            self.is_alive = True

    def __str__(self):
        return f""

    def __repr__(self):
        return f""

    @classmethod
    def create_lannister():
        pass


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, \
        Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()
