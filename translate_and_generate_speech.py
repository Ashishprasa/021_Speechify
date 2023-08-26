# Import libraries
from googletrans import Translator
from gtts import gTTS

# Initialize Translator
translator = Translator()

# Function to convert a list of strings to a single string separated by ". "


def listToString(s):
    separator = ". "
    return separator.join(s)


# Text to be translated
source_text = "This is the source text that you want to translate."

# Translate the text to Hindi
translations = translator.translate(source_text, dest='hi')

# Extract translated text and store in a list this method is called listcompression
translated_list = [translation.text for translation in translations]

# Convert the list of translated strings to a single string
translated_text = listToString(translated_list)

# Generate Hindi speech from the translated text
voice = gTTS(text=translated_text, lang='hi', slow=False)

# Save the generated speech as an MP3 file
voice.save("VoiceText.mp3")
