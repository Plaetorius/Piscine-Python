from S1E9 import Character
import sys


class Baratheon(Character):
    """Baratheon class. Implementation of the abstract Character class with its
    own constructor (not using Character's).

    Args:
        Character (ABC): The abstract Character class
    """
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
            print("first_name must be a string. Setting it to 'default'",
                  file=sys.stderr)
            self.first_name = 'default'
        if isinstance(is_alive, bool):
            self.is_alive = is_alive
        else:
            print("is_alive must be bool. Setting it to True",
                  file=sys.stderr)
            self.is_alive = True
        self.family_name = self.__class__.__name__
        self.eyes = "brown"
        self.hair = "dark"

    def __str__(self):
        """Returns the string version of a Baratheon"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        """Returns the string representation of a Baratheon"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def die(self):
        """Sets the is_alive attribute to False"""
        self.is_alive = False


class Lannister(Character):
    """Lannister class. Implementation of the abstract Character class with its
    own constructor (not using Character's). Can create new Lannister using the
    create_lannister() method.

    Args:
        Character (ABC): The abstract Character class
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor of the Lannister class. Does checks on whether the given
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
            print("first_name must be a string. Setting it to 'default'",
                  file=sys.stderr)
            self.first_name = 'default'
        if isinstance(is_alive, bool):
            self.is_alive = is_alive
        else:
            print("is_alive must be bool. Setting it to True",
                  file=sys.stderr)
            self.is_alive = True
        self.family_name = self.__class__.__name__
        self.eyes = "blue"
        self.hair = "light"

    def __str__(self):
        """Returns the string version of a Lannister"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        """Returns the string representation of a Lannister"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Creates a Lannister from the Class not from an Instance

        Args:
            first_name (str): The name of the Lannister to be created
            is_alive (bool, optional): Life status. Defaults to True.

        Returns:
            Lannister: Instance of a Lannister with the given arguments
        """
        return cls(first_name, is_alive)

    def die(self):
        """Sets the is_alive attribute to False"""
        self.is_alive = False


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
