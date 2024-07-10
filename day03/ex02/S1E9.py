from abc import ABC, abstractmethod
import sys


class Character(ABC):
    """Character class, with a first_name (str), an is_alive (bool) attribute
    and method (returns the is_alive attribute), and the abstract method die(),
    that sets is_alive (attribute) to False


    Args:
        ABC (Abstract Class): Generic Abstract Class from the ABC library"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor of the Character class. Does checks on whether the given
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

    @abstractmethod
    def die():
        pass


class Stark(Character):
    """Stark class. Inherits from the Character class and implements the die()
    abstract method."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor of the Class Stark. Calls the constructor of its
        parent Class (Character) with the arguments first_name and is_alive

        Args:
            first_name (str): the first name of the Stark
            is_alive (bool): the life status of the Stark. Defaults to True."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Sets the is_alive attribute to False"""
        self.is_alive = False


def main():
    """Main function of the  program. Runs tests from the subject."""
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    try:
        hodor = Character("hodor")
        print(hodor)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
