from chat_to_speech.core.data_types import AZURE_VOICES


def tts(text: str, voice: str):
    """
    Call the Azure text-to-speech API, save an audio file of an utterance.
    """
    voice = AZURE_VOICES[voice]
