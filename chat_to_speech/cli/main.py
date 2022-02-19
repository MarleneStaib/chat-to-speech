# pylint: disable=missing-function-docstring

import click

@click.group()
def cli():
    pass


def miri():
    pass


cli.add_command(miri)


def main():
    return cli()


if __name__ == "__main__":
    main()