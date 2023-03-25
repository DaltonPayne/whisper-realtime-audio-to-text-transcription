import io
import os
import pyaudio
import openai
import random
import string
import tempfile
import wave
from pydub import AudioSegment
import audioop


os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

openai.api_key = os.environ["OPENAI_API_KEY"]

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 0  # length of audio to record
FILE_NAME = "recorded_audio.wav"  # name of audio file

audio = pyaudio.PyAudio()

stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)

print("Speak now...")

frames = []
silence_counter = 0

while silence_counter < 40:
    data = stream.read(CHUNK)
    frames.append(data)
    # calculate root mean square to check for silence
    rms = audioop.rms(data, 2)
    if rms < 150:
        silence_counter += 1
    else:
        silence_counter = 0

stream.stop_stream()
stream.close()
audio.terminate()

# save audio as WAV file
with wave.open(FILE_NAME, "wb") as wav_file:
    wav_file.setnchannels(CHANNELS)
    wav_file.setsampwidth(audio.get_sample_size(FORMAT))
    wav_file.setframerate(RATE)
    wav_file.writeframes(b''.join(frames))

# convert WAV file to MP3 format
sound = AudioSegment.from_file(FILE_NAME)
sound.export("recorded_audio.mp3", format="mp3")

# transcribe audio using OpenAI's GPT-3 API
with open("recorded_audio.mp3", "rb") as audio_file:
    response = openai.Audio.transcribe("whisper-1", audio_file, file_name="recorded_audio.mp3")
    text = response["text"]
    if text.strip():
        print(text.strip())
