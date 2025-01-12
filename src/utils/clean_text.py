import re

from unidecode import unidecode


def clean_web_text(text):
    # Convert Unicode characters to ASCII equivalents
    text = unidecode(text)

    # Replace multiple newlines and spaces with a single newline
    cleaned_text = re.sub(r'(\s*\n\s*)+', '\n', text)
    cleaned_text = re.sub(r'(\s*\r\n\s*)+', '\n', cleaned_text)
    return cleaned_text


def clean_text_remove_newlines(text):
    # Remove newlines and extra spaces
    cleaned_text = re.sub(r'(\s*\n\s*)+', '*', text)
    cleaned_text = re.sub(r'(\s*\r\n\s*)+', '', cleaned_text)
    return cleaned_text
