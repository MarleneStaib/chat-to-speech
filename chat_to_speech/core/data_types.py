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
