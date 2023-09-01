# Text-to-Speech Translation Program

This is a Python program that translates a given text into Hindi using Google Translate and then converts the translated text into speech using Google Text-to-Speech (gTTS). The generated speech is saved as an MP3 audio file.

## Prerequisites

Before running the program, you need to have the following libraries installed:

- `googletrans`: A Python wrapper around the Google Translate API.
- `gtts`: Google Text-to-Speech, which converts text into speech.

You can install these libraries using the following commands:

```
pip install googletrans
pip install gtts
```

## Usage

1. Open the Python script `translate_and_generate_speech.py` in a code editor of your choice.

2. Customize the `source_text` variable with the text you want to translate and generate speech for.

3. Run the script using a Python interpreter:

```
python translate_and_generate_speech.py
```

4. The program will translate the provided text into Hindi and save the generated speech as an MP3 file named `VoiceText.mp3` in the same directory.

## Contributing

Feel free to contribute to this project by suggesting improvements or adding new features. You can fork this repository, make your changes, and then submit a pull request. 🙂