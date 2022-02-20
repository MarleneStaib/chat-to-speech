import os
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
@click.option("--output-dir", type=click.Path(), default="data/new")
def miri(url, output_dir):
    """
    Parse Miri formatted conversations html and run it through the conversation TTS.
    See https://intelligence.org/2021/11/15/ngo-and-yudkowsky-on-alignment-difficulty/
    for an example blog post.
    """
    data = get_html(url)
    utts = parse_html_miri_conversations(data)

    os.makedirs(output_dir, exist_ok=True)
    
    # Run TTS for "voice intros" - so that people know who is who
    for person, voice in PERSON_TO_VOICE.items():
        if person not in ["Narrator", "Other"]:
            text = f"Hi. I'll be reading the voice of {person}."
            fname = os.path.join(output_dir, f"voice_intro_{person}.wav")
            tts(text=text, voice=voice, filename=fname)

    # Run TTS for the chat utterances
    for utt in utts:
        voice = PERSON_TO_VOICE[utt.speaker]
        fname = os.path.join(output_dir, f"utt_{utt.index}.wav")
        tts(text=utt.text, voice=voice, filename=fname)
