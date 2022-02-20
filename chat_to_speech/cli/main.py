# pylint: disable=missing-function-docstring

import click
from chat_to_speech.cli.miri import miri


@click.group()
def cli():
    """
    HTML conversations TTS CLI.
    """
    pass


cli.add_command(miri, "miri")


if __name__ == "__main__":
    cli()
