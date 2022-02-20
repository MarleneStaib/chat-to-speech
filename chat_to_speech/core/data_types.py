import attr


@attr.s
class Utterance:
    speaker = attr.ib(type=str)
    text = attr.ib(type=str)
    index = attr.ib(type=int)


@attr.s
class TTSVoice:
    name = attr.ib(type=str)
    language = attr.ib(type=str)
    style = attr.ib(type=str, default=None)
    default_speech_rate = attr.ib(type=str, default=None)
    description = attr.ib(type=str, default=None)


# A selection of American voices that seem suitable for male/male conversation pairs/trios
# I've selected the "main speakers 1-3" to be clearly distinguishable from one another
# And of higher quality, among the options.
AZURE_VOICES = {
    "Guy": TTSVoice(
        name="en-US-GuyNeural",
        language="en-US",
        style="newscast",
        default_speech_rate="10%",
        description="Good presenter/narrator voice",
    ),
    "Christopher": TTSVoice(
        name="en-US-ChristopherNeural",
        language="en-US",
        description="Voice for main male speaker 1.",
    ),
    "Brandon": TTSVoice(
        name="en-US-BrandonNeural",
        language="en-US",
        description="Voice for main male speaker 2.",
    ),
    "Liam": TTSVoice(
        name="en-CA-LiamNeural",
        language="en-CA",
        description="Voice for main male speaker 3.",
    ),
    "Jacob": TTSVoice(
        name="en-US-JacobNeural",
        language="en-US",
        description="Voice for less often used speakers.",
    ),
    "Eric": TTSVoice(
        name="en-US-EricNeural",
        language="en-US",
        description="Very similar to main speaker 1 - backup voice.",
    ),
}
