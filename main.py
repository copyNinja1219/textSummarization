import os
from google.cloud import speech
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ageless-period-303512-92005536c5f9.json'
speech_client = speech.SpeechClient()

media_file_name = 'fun-in-osaka_Ck8Pwxzm.mp3'


with open(media_file_name, 'rb') as f1:
    byte_data = f1.read()
audio_mp3 = speech.RecognitionAudio(content=byte_data)


config_mp3 = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation=True,
    language_code='en-US'
)

response_mp = speech_client.recognize(
    config=config_mp3,
    audio=audio_mp3
)

print(response_mp)
