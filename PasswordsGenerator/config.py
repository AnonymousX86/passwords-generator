# -*- coding: utf-8 -*-
from rich.console import Console


class Config:
    """
    Class to store the configuration of the program.
    """
    def __init__(
            self,
            use_lowercase: bool,
            use_uppercase: bool,
            use_numbers: bool,
            use_specials: bool,
            quantity: int,
            length: int
    ):
        self.__use_lowercase = use_lowercase
        self.__use_uppercase = use_uppercase
        self.__use_numbers = use_numbers
        self.__use_specials = use_specials
        self.__quantity = quantity
        self.__length = length

    def __str__(self):
        return '<Config: ' + \
               'a' if self.__use_lowercase \
            else '' + 'A' if self.__use_uppercase \
            else '' + '0' if self.__use_numbers \
            else '' + '!' if self.__use_specials \
            else '' + f' Quantity: {self.__quantity} Length: {self.__length}>'

    @property
    def use_lowercase(self) -> bool:
        """
        :return: True if the lowercase characters are used, False otherwise.
        """
        return self.__use_lowercase

    @property
    def use_uppercase(self) -> bool:
        """
        :return: True if the uppercase characters are used, False otherwise.
        """
        return self.__use_uppercase

    @property
    def use_numbers(self) -> bool:
        """
        :return: True if the numbers are used, False otherwise.
        """
        return self.__use_numbers

    @property
    def use_specials(self) -> bool:
        """
        :return: True if the special characters are used, False otherwise.
        """
        return self.__use_specials

    @property
    def quantity(self) -> int:
        """
        :return: The quantity of the passwords to generate.
        """
        return self.__quantity

    @property
    def length(self) -> int:
        """
        :return: The length of the passwords to generate.
        """
        return self.__length


def create_config(console: Console) -> Config:
    """
    Create a Config object from the user input.
    :param console: Console object to display the messages.
    :return: Config object.
    """
    choice_yes = ('y', 'yes')
    choice_no = ('n', 'no')

    use_user_config = None
    while not type(use_user_config) == bool:
        use_user_config = console.input(':gear: Do you want to use custom config? [Y/n] ')
        if not use_user_config:
            use_user_config = 'y'
        if (lower := use_user_config.lower()) in choice_yes:
            use_user_config = True
        elif lower in choice_no:
            use_user_config = False

    # Ask for config
    if use_user_config:
        to_config_bool = (
            'lowercase',
            'uppercase',
            'numbers',
            'specials',
        )
        to_config_int = (
            'How many passwords do you want?',  # quantity
            'How long should be each password?',  # length
        )
        raw_config = []

        # Config boolean values
        for key in to_config_bool:
            value = None
            while not type(value) == bool:
                value = console.input(f':gear: Do you want to use {key}? [Y/n] ')
                if not value:
                    value = 'y'
                if (value := value.lower()) in choice_yes:
                    value = True
                elif value in choice_no:
                    value = False
            raw_config.append(value)

        # Config integer values
        for key in to_config_int:
            value = 0
            while not 1 <= value <= 100:
                value = console.input(f':gear: {key} [1-100] ')
                try:
                    value = int(value)
                except ValueError:
                    value = 0
            raw_config.append(value)

        config = Config(*raw_config)

    # Load default config
    else:
        console.print(':inbox_tray: OK, using default config')
        config = Config(
            True,
            True,
            True,
            True,
            4,
            12
        )

    return config
