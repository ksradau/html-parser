import sys
import requests
from bs4 import BeautifulSoup
from collections import Counter
import pymorphy2
import string


def get_urls_from_file():
    with open(sys.argv[1], 'r') as f:
        list_of_urls = [line.rstrip('\n') for line in f]
    return list_of_urls


def get_text_from_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    text = soup.get_text()
    return text


def get_clean_text(text):
    lower_text = text.lower()
    text_without_punc = lower_text.translate(str.maketrans('', '', string.punctuation))

    clean_text = text_without_punc.replace('—', '').replace('<', '').replace('>', '').replace('–', '').replace('»', '').replace('«', '')
    return clean_text


def get_top_words_from_text(clean_text, number_of_words):
    words = clean_text.split()

    morph = pymorphy2.MorphAnalyzer()
    ignore_words = {'INTJ', 'PRCL', 'CONJ', 'PREP'}

    words = [morph.parse(w)[0].normal_form for w in words if morph.parse(w)[0].tag.POS not in ignore_words and w.isdigit() is not True]
    most_common_words = Counter(words).most_common(number_of_words)

    return most_common_words


def beautiful_output_for_common_words(common_words):
    list_of_words = [word[0] for word in common_words]
    return list_of_words
