from setuptools import find_packages, setup

INSTALL_REQUIRES = [
    "bs4==0.0.1"
    "click==7.1.2",
]


config = {
    "name": "chat-to-speech",
    "version": "0.0.1",
    "description": "Module for converting chat logs in html format to speech using TTS",
    "author": "Marlene Staib",
    "author_email": "marlene.staib@gmail.com",
    "packages": find_packages(include=["chat_to_speech", "chat_to_speech.*"]),
    "install_requires": INSTALL_REQUIRES,
    "entry_points": {
        "console_scripts": ["chat-to-speech=chat_to_speech.cli.main:main"],
    },
}

setup(**config)