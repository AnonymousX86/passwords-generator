# -*- coding: utf-8 -*-
from random import choice

from rich.console import Console

if __name__ == '__main__':
    console = Console()
    console.rule('Passwords Generator')

    LOWER = [*'abcdefghijklmnopqrstuvwxyz']
    UPPER = [x.upper() for x in LOWER]
    NUMBERS = [*'0123456789']
    SPECIALS = [*'!@#$%^&*()-_=+[]{};:,.<>?']

    QUANTITY = int(console.input(':1234: Quantity: '))
    LENGTH = int(console.input(':straight_ruler: Length: '))
    CONFIG = dict(
        lower=True,
        upper=True,
        numbers=True,
        specials=True
    )

    source = []
    if CONFIG['lower']:
        source += LOWER
    if CONFIG['upper']:
        source += UPPER
    if CONFIG['numbers']:
        source += NUMBERS
    if CONFIG['specials']:
        source += SPECIALS

    passwords = []

    if source:
        for _ in range(QUANTITY):
            phrase = ''
            for _ in range(LENGTH):
                phrase += choice(source)
            passwords.append(phrase)

    if passwords:
        console.print(':closed_lock_with_key: Your passwords:')
        for password in passwords:
            console.print(u' [bold]\u00b7[/] [white]{}'.format(password))
    else:
        console.print('Wrong config - no passwords to show.')
