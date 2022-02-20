import click
from chat_to_speech.core.html_parsing import get_html, parse_html_miri_conversations
from chat_to_speech.core.tts import tts


PERSON_TO_VOICE = {
    "Narrator": "Guy",
    "Yudkowsky": "Christopher",
    "Ngo": "Brandon",
    "Soares": "Liam",
    "Other": "Jacob",
}


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

    # Run TTS
    for utt in utts:
        voice = PERSON_TO_VOICE[utt.speaker]
        tts(text=utt.text, voice=voice)
