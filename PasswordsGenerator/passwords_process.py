# -*- coding: utf-8 -*-
from random import choice

from rich.console import Console

from PasswordsGenerator.config import Config


def generate(config: Config) -> list[str] | RuntimeError:
    """
    Generate passwords.
    :param config: Config object.
    :return: List of generated passwords or RuntimeError if passed wrong configuration.
    """
    lower = [*'abcdefghijklmnopqrstuvwxyz']
    upper = [x.upper() for x in lower]
    numbers = [*'0123456789']
    specials = [*'!@#$%^&*()-_=+[]{};:,.<>?']

    source = []
    if config.use_lowercase:
        source += lower
    if config.use_uppercase:
        source += upper
    if config.use_numbers:
        source += numbers
    if config.use_specials:
        source += specials

    if not source:
        return RuntimeError('Incorrect configuration')

    passwords = []
    for _ in range(config.quantity):
        phrase = ''
        for _ in range(config.length):
            phrase += choice(source)
        passwords.append(phrase)

    return passwords


def ask_for_saving(console: Console) -> (bool, str):
    """
    Ask the user if he wants to save the passwords to a file.
    :param console: Console object to display the messages.
    :return: True and file name to save passwords to if the user wants to save the passwords to a file,
             False and None otherwise.
    """
    should_save_to_file = None
    while not type(should_save_to_file) == bool:
        value = console.input(
            ':memo: Do you want to save passwords to file? [Y/n] '
        )
        if not value:
            value = 'y'
        if (lower := value.lower()) in ('y', 'yes'):
            should_save_to_file = True
        elif lower in ('n', 'no'):
            should_save_to_file = False
    file_name = None
    if should_save_to_file:
        file_name = ''
        while not file_name:
            file_name = console.input(
                ':memo: Enter file name to save passwords to: '
            )
    return should_save_to_file, file_name


def save_to_file(file_name: str, passwords_list: list[str]) -> (bool, Exception | None):
    """
    Save the passwords list to a file.
    :param file_name: the name of the file
    :param passwords_list: the passwords list
    :return: True and None if the file was saved successfully, False and Exception otherwise
    """
    try:
        with open(file_name, 'w') as file:
            for password in passwords_list:
                file.write(password + '\n')
        return True, None
    except Exception as e:
        return False, e
