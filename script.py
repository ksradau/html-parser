from functions import get_urls_from_file, get_text_from_page, get_clean_text, get_top_words_from_text, print_beautiful_output
from functions import ParserError
import sys


NUMBER_OF_WORDS = 10


def to_parse():
    urls = get_urls_from_file()
    for url in urls:
        try:
            text = get_text_from_page(url)
            clean_text = get_clean_text(text)
            list_of_words = get_top_words_from_text(clean_text, NUMBER_OF_WORDS)
            print_beautiful_output(list_of_words, url)
        except ParserError:
            print("Something was wrong during parser's work")


def main():
    try:
        to_parse()
    except Exception:
        return 1
    else:
        return 0


if __name__ == "__main__":
    sys.exit(main())
