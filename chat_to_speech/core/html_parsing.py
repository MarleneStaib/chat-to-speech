import requests
import bs4
import re

from chat_to_speech.core.data_types import Utterance


def get_html(url: str):
    """
    Retrieve an html file from a URL.
    """
    data = requests.get(
        url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        },
    )
    return data


def parse_text_for_tts(text):
    """
    Parse text to feed into the TTS API:
        * Add punctuation to paragraphs not ending in a final stop (e.g., titles)
        * Add breaks after each paragraph
        * Read quotes as "quote/end quote"
    """
    # Strip bad symbols
    text = re.sub(r"\xa0", "", text)
    text = re.sub(" ?-> ?", " to ", text)

    # Punctuating paragraphs
    def punctuate(paragraph):
        if paragraph[-1] in ".!?:":
            return paragraph
        return paragraph + "."

    paragraphs = text.split("\n")
    paragraphs = [p.strip() for p in paragraphs]
    paragraphs = [p for p in paragraphs if p]
    paragraphs = [punctuate(p) for p in paragraphs]
    text = " ".join(paragraphs)

    # Reading out quotes
    def read_quotes(text):
        open_quotes = False
        new_text = ""

        for char in text:
            if char in [r"”", r'"', r"“"]:
                if not open_quotes:
                    open_quotes = True
                    new_text += ', quote, "'
                else:
                    open_quotes = False
                    new_text += '", end quote, '
            else:
                new_text += char

        # Remove additional commas before full stops
        new_text = re.sub(", \.", ".", new_text)
        return new_text

    text = read_quotes(text)

    return text


def parse_html_miri_conversations(html_data: requests.models.Response):
    """
    Parse an html response in the form of the Miri conversations into a set of
    Utterance objects.
    """
    utterances = []
    speaker = "Narrator"

    if not html_data:
        return utterances

    parser = bs4.BeautifulSoup(html_data.text, "html.parser")

    def text_selector(tag):
        chat_blob = (
            tag.name == "div"
            and tag.has_attr("class")
            and "accordion-group" in tag.attrs["class"]
        )
        headers = tag.name in ["h1", "h2", "h3"]
        return chat_blob or headers

    utterance_blobs = parser.find_all(text_selector)

    for i, utt_blob in enumerate(utterance_blobs):
        text = utt_blob.get_text().strip()

        # Parse out the speaker
        # For titles, always use the narrator as speaker
        if "accordion-group" not in utt_blob.attrs.get("class", []):
            speaker = "Narrator"
        # For chatblobs, parse out the speaker
        else:
            match = re.search(r"^\[(.*?)\](?:\[.*\])?", text)
            if match:  # if no match, keep the speaker from before
                speaker = match[1]
                text = text[match.span()[1] :].strip()  # remove speaker info from text

        # Parse into TTS-able utterances
        text = parse_text_for_tts(text)
        utt = Utterance(text=text, speaker=speaker, index=i)
        utterances.append(utt)

    return utterances
