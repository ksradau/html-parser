import sys
import requests
from bs4 import BeautifulSoup
from collections import Counter


def get_urls_from_file():
    with open(sys.argv[1], 'r') as f:
        list_of_urls = [line.rstrip('\n') for line in f]
    return list_of_urls


def get_text_from_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    text = soup.get_text()
    return text


def get_top_words_from_text(text, number_of_words):
    words = text.lower().split()
    most_common_words = Counter(words).most_common(number_of_words)
    return most_common_words #list of tuples


def beautiful_output_for_common_words(common_words):
    list_of_words = [word[0] for word in common_words]
    return list_of_words
