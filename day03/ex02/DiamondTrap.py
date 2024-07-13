from S1E7 import Baratheon, Lannister
import sys


class King(Baratheon, Lannister):
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor of the King class. Does checks on whether the given
        arguments are of correct type. If not, raises a TypeError and sets
        default values.

        Args:
            first_name (str): The name of the Character
            is_alive (bool, optional): The life status of the Character.
                Defaults to True.
        """
        super().__init__(first_name, is_alive)
        # Get the 'Baratheon' family name using the Method Resolution Order
        # Element 0 is King, 1 is Baratheon, 2 is Lannister
        self.family_name = self.__class__.__mro__[1].__name__

    def set_eyes(self, eyes_color: str):
        """Set eyes field to whatever string as been passed in parameters

        Args:
            eyes_color (str): the color for the eyes. Defaults at brown.
        """
        if isinstance(eyes_color, str):
            self.eyes = eyes_color
        else:
            print("eyes_color must be a string. Setting it to 'brown'",
                  file=sys.stderr)
            self.eyes = 'brown'

    def set_hair(self, hair_color: str):
        """Set hair field to whatever string as been passed in parameters

        Args:
            hair_color (str): the color for the hair. Defaults at dark.
        """
        if isinstance(hair_color, str):
            self.hair = hair_color
        else:
            print("hair_color must be a string. Setting it to 'dark'",
                  file=sys.stderr)
            self.hair = 'dark'

    def get_eyes(self):
        """Getter for the eyes"""
        return self.eyes

    def get_hair(self):
        """Getter for the hair"""
        return self.hair


def main():
    """Main function. Run subjects tests"""
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hair("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hair())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
