from googletrans import Translator, LANGUAGES
import pyperclip
import os

location_of_script = os.path.dirname(os.path.abspath(__file__))
file = open(location_of_script + "/settings.conf", "r")
for line in file:
    if line.startswith("DESTINATION_LANG"):
        dest_lang = line.split("=")[1].strip()
    if line.startswith("SRC_LANG"):
        src_lang = line.split("=")[1].strip()

translator = Translator()
text_to_translate = pyperclip.paste()
translated_text = translator.translate(text_to_translate, dest=dest_lang, src=src_lang).text
pyperclip.copy(translated_text)
