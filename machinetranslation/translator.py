"""Translates text from one language to another using IBM Watson Translator service"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

ENV_FILE = "/home/project/python-for-ai-development-project/language-translator.ibm-credentials.env"
LANGUAGE_TRANSLATOR: LanguageTranslatorV3 = None

with open(ENV_FILE, encoding='utf-8') as env_file:
    for line in env_file:
        if line.startswith('#') or not line.strip():
            continue
        key, value = line.strip().split('=', 1)
        os.environ[key] = value

def get_language_translator ():
    """Authentication on IBM Watson Translator service and configures the translator class"""
    global LANGUAGE_TRANSLATOR
    if LANGUAGE_TRANSLATOR is None:
        authenticator = IAMAuthenticator(os.environ.get('LANGUAGE_TRANSLATOR_APIKEY'))
        LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
            version=os.environ.get('LANGUAGE_TRANSLATOR_VERSION'),
            authenticator=authenticator
        )
        LANGUAGE_TRANSLATOR.set_service_url(os.environ.get('LANGUAGE_TRANSLATOR_URL'))
    return LANGUAGE_TRANSLATOR

def englishtofrench (text: str = None):
    """Returns french translation of a given text in english"""
    string: str = None
    try:
        translator = get_language_translator()
        translation_response = translator.translate(text=text, source='en', target='fr')
        translation = translation_response.get_result()
        string = translation['translations'][0]['translation']
    except ValueError:
        print("ValueError")
    return string

def englishtogerman (text: str = None):
    """Returns german translation of a given text in english"""
    string: str = None
    try:
        translator = get_language_translator()
        translation_response = translator.translate(text=text, source='en', target='de')
        translation = translation_response.get_result()
        string = translation['translations'][0]['translation']
    except ValueError:
        print("ValueError")
    return string
