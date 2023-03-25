# Audio-to-Text Transcription

This script records audio input from a microphone and transcribes it into text using OpenAI's GPT-3 API.

## Requirements

- Python 3.6+
- [openai](https://pypi.org/project/openai/) library
- [pyaudio](https://pypi.org/project/PyAudio/) library
- [pydub](https://pypi.org/project/pydub/) library
- [audioop](https://docs.python.org/3/library/audioop.html) library

## Installation

1. Clone the repository:
$ git clone https://github.com/your_username/audio-to-text-transcription.git
$ cd audio-to-text-transcription

2. Install the required libraries:
$ pip install openai pyaudio pydub

## Usage
1. Replace `YOUR_API_KEY` with your OpenAI API key in the `audio_transcription.py` script:

```python
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

2. Run the script:
$ python audio_transcription.py

3. Speak into your microphone when prompted. The script will continuously record audio and stop recording after detecting 4 seconds of silence. The transcribed text will be printed to the console.