from dotenv import dotenv_values
import azure.cognitiveservices.speech as speechsdk

from chat_to_speech.core.data_types import AZURE_VOICES
from chat_to_speech.core.auth import get_token


AZURE_SUBSCRIPTION_KEY = dotenv_values(".env")["AZURE_SUBSCRIPTION_KEY"]


def tts(text: str, voice: str, filename: str):
    """
    Call the Azure text-to-speech API, save an audio file of an utterance.
    """
    voice = AZURE_VOICES[voice]
    speech_config = speechsdk.SpeechConfig(
        subscription=AZURE_SUBSCRIPTION_KEY, region="westeurope"
    )

    # Speech config
    speech_config.speech_synthesis_language = voice.language
    speech_config.speech_synthesis_voice_name = voice.name

    # Save audio config
    audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config
    )
    synthesizer.speak_text_async(text)
