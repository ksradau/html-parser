import sys
import requests
from bs4 import BeautifulSoup
from collections import Counter
import pymorphy2
import string
import argparse
from pathlib import Path


def get_args_from_console():
    p = argparse.ArgumentParser(description="Args for HTML parser")
    p.add_argument("--file", metavar="Path to your file", dest="file_with_urls", type=str)
    app_args = p.parse_args()
    if not app_args.file_with_urls:
        p.print_help()
        sys.exit(-1)
    return app_args


def get_file_with_urls():
    app_args = get_args_from_console()
    file_with_urls = Path(app_args.file_with_urls)
    if not file_with_urls.is_file():
        raise InputDataError("Something wrong with your input data. It must be file that contains URLs.")
    return file_with_urls


def get_urls_from_file():
    file_with_urls = get_file_with_urls()
    with open(file_with_urls, 'r') as f:
        list_of_urls = [line.rstrip('\n') for line in f]
    return list_of_urls


def get_text_from_page(url):
    r = requests.get(url)
    if r.status_code != 200:
        raise UrlError("Something wrong with URL ", url)
    soup = BeautifulSoup(r.text, 'html.parser')
    text = soup.get_text()
    return text


def get_clean_text(text):
    lower_text = text.lower()
    text_without_punc = lower_text.translate(str.maketrans('', '', string.punctuation))
    clean_text = text_without_punc.replace('—', '').replace('–', '').replace('»', '').replace('«', '')
    return clean_text


def get_top_words_from_text(clean_text, number_of_words):
    words = clean_text.split()
    morph = pymorphy2.MorphAnalyzer()
    ignore_words = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
    words = [morph.parse(w)[0].normal_form for w in words if morph.parse(w)[0].tag.POS not in ignore_words and not w.isdigit()]
    most_common_words = Counter(words).most_common(number_of_words)
    list_of_words = [word[0] for word in most_common_words]
    return list_of_words


def print_beautiful_output(list_of_words, url):
    print("Most common for ", url )
    print(*list_of_words)
    print("\n~ ~ ~ ~ ~ ~")


class ParserError(Exception):
    pass


class UrlError(ParserError):
    pass


class InputDataError(ParserError):
    pass