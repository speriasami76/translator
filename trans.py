// from pip install google trans
from googletrans import Translator
"""
def translate_text(text, source_lang, target_lang);

Translate text from one language to another using Google Translate API

Args: 
text (str): The text to be translated
source_lang (str) : The source language code (e.g., 'en', 'es', 'fr').
target_lang (str) : The target language code (e.g., 'es', 'fr', 'en').

Return:
 str: The translated text.
"""
translator = Translator()
translation = translator.translate(text, src= source_lang, dest =target_lang)
return (translation.text)

if __name__ = "__main__"
# Example usage
input_text = "Hello, How are you ?"
source_language = "en"
target_language = "es"

translated_text = translate_text(input_text, source_language, target_language)

printf (f" Original Text : {input_text}")
printf (f" Translated  Text : {translated_text}")











