import click
from chat_to_speech.core.html_parsing import get_html, parse_html_miri_conversations


@click.command()
@click.argument("url", type=str)
def miri(url):
    """
    Parse Miri formatted conversations html and run it through the conversation TTS.
    See https://intelligence.org/2021/11/15/ngo-and-yudkowsky-on-alignment-difficulty/
    for an example blog post.
    """
    data = get_html(url)
    utts = parse_html_miri_conversations(data)
