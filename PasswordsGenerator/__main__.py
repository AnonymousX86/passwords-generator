# -*- coding: utf-8 -*-
from rich.console import Console

from PasswordsGenerator.config import create_config
from PasswordsGenerator.passwords_process import generate, save_to_file, ask_for_saving

if __name__ == '__main__':
    console = Console()
    console.rule('Passwords Generator')

    config = create_config(console)

    passwords = generate(config)
    if isinstance(passwords, RuntimeError):
        console.print(':x: Wrong config - no passwords to show.')
    elif not passwords:
        console.print(':x: Something bad happened - no passwords to show.')
    else:
        console.print(':locked_with_key: Your passwords:')
        for password in passwords:
            console.print(u' [bold]\u00b7[/bold] [white]{}'.format(password))

        should_save_to_file, file_name = ask_for_saving(console)
        if should_save_to_file:
            try:
                with open(file_name, 'x') as _:
                    pass
            except FileExistsError:
                pass
            try:
                save_to_file(file_name, passwords)
            except PermissionError:
                console.print(':x: Permission denied.')
            else:
                console.print(f':white_check_mark: Your passwords saved to file: [bold italic]{file_name}[/].')

    console.print(':wave: Bye!')
    console.print(':man_technologist: I was made by [italic]Jakub Suchenek[/]')
    console.print(
        ':link: Check out my GitHub: [link=https://github.com/AnonymousX86/passwords-generator]'
        'https://github.com/AnonymousX86/passwords-generator[/]'
    )
    console.print('')
